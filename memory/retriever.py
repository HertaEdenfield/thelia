"""Thelia Memory Retriever 1.1.0

Model-neutral, dependency-free reference implementation.
It searches the compact recall index first and loads only ranked entry files.
It is intentionally a retrieval component, not a chat agent or identity authority.
"""
from __future__ import annotations

import json
import math
import re
import unicodedata
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
INDEX_PATH = ROOT / "index.json"
ALIASES_PATH = ROOT / "aliases.json"
RETRIEVAL_PATH = ROOT / "retrieval.json"
WORD_RE = re.compile(r"[\wÀ-ÿ]+", re.UNICODE)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).casefold()
    return re.sub(r"\s+", " ", text).strip()


def tokens(text: str) -> set[str]:
    return set(WORD_RE.findall(normalize(text)))


def token_overlap(query: str, value: str) -> float:
    q, v = tokens(query), tokens(value)
    if not q or not v:
        return 0.0
    return len(q & v) / max(1, len(q | v))


def phrase_similarity(query: str, value: str) -> float:
    q, v = normalize(query), normalize(value)
    if not q or not v:
        return 0.0
    if q == v:
        return 1.0
    if q in v or v in q:
        return 0.9
    return SequenceMatcher(None, q, v).ratio()


def field_score(query: str, values: list[str]) -> float:
    if not values:
        return 0.0
    overlap = max(token_overlap(query, v) for v in values)
    phrase = max(phrase_similarity(query, v) for v in values)
    return min(1.0, 0.65 * overlap + 0.35 * phrase)


def recency_score(iso_date: str | None) -> float:
    if not iso_date:
        return 0.0
    try:
        age = max(0, (date.today() - date.fromisoformat(iso_date)).days)
    except ValueError:
        return 0.0
    return math.exp(-age / 45.0)


def confidence_score(value: str) -> float:
    return {"high": 1.0, "medium": 0.65, "low": 0.35}.get(value, 0.5)


def expand_query(query: str, alias_map: dict[str, Any]) -> list[str]:
    """Add aliases that occur in the query without deleting original wording."""
    q = normalize(query)
    expansions = [q]
    for mapping in alias_map.get("maps", []):
        aliases = mapping.get("aliases", [])
        if any(normalize(alias) in q for alias in aliases):
            expansions.append(mapping.get("canonical", ""))
    return list(dict.fromkeys(x for x in expansions if x))[:12]


def best_field(query_forms: list[str], values: list[str]) -> float:
    return max((field_score(q, values) for q in query_forms), default=0.0)


def retrieve(query: str, limit: int = 5) -> list[dict[str, Any]]:
    """Return the smallest useful ranked memory set.

    Stage 1 reads only the compact index and alias map. Stage 2 opens full
    entry files only for candidates that survive ranking. Raw keys improve
    recall but are never returned as memory content by themselves.
    """
    index = load_json(INDEX_PATH)
    alias_map = load_json(ALIASES_PATH)
    policy = load_json(RETRIEVAL_PATH)
    query_forms = expand_query(query, alias_map)
    weights = {
        "semantic": 0.30,
        "exact_phrase": 0.18,
        "raw": 0.16,
        "alias": 0.10,
        "entity": 0.08,
        "recency": 0.07,
        "specificity": 0.05,
        "confidence": 0.04,
        "relation": 0.02,
    }
    ranked: list[tuple[float, dict[str, Any]]] = []

    for entry in index.get("entries", []):
        semantic = best_field(query_forms, entry.get("semantic_keys", []))
        raw = best_field(query_forms, entry.get("raw_keys", []))
        alias = best_field(query_forms, entry.get("aliases", []))
        entity = best_field(query_forms, entry.get("entities", []))
        exact = max(
            (phrase_similarity(q, x)
             for q in query_forms
             for x in entry.get("semantic_keys", []) + entry.get("raw_keys", []) + entry.get("aliases", [])),
            default=0.0,
        )
        specificity = min(1.0, len(tokens(query)) / 8.0)
        # The compact index intentionally does not carry dates. Recency and
        # relationship signals are therefore applied after candidate loading.
        score = (
            semantic * weights["semantic"]
            + exact * weights["exact_phrase"]
            + raw * weights["raw"]
            + alias * weights["alias"]
            + entity * weights["entity"]
            + specificity * weights["specificity"]
            + confidence_score(entry.get("confidence", "medium")) * weights["confidence"]
        )
        if exact >= 0.95:
            score += 0.15
        if entry.get("status") == "historical":
            score -= policy.get("scoring", {}).get("historical_penalty", 0.10)
        if entry.get("status") == "deprecated":
            score -= policy.get("scoring", {}).get("deprecated_penalty", 0.25)
        ranked.append((score, entry))

    ranked.sort(key=lambda item: item[0], reverse=True)
    threshold = policy.get("scoring", {}).get("minimum_score", 0.34)
    candidate_limit = min(max(limit * 2, 8), 16)
    candidates = [(score, entry) for score, entry in ranked if score >= threshold][:candidate_limit]

    results: list[dict[str, Any]] = []
    for score, entry in candidates:
        ref = entry.get("content_ref")
        if not ref:
            continue
        path = ROOT / ref.removeprefix("memory/")
        if not path.exists():
            continue
        memory = load_json(path)
        final_score = score
        final_score += recency_score(memory.get("updated") or memory.get("created")) * weights["recency"]
        final_score += confidence_score(memory.get("confidence", entry.get("confidence", "medium"))) * weights["confidence"]
        results.append({"id": entry["id"], "score": round(final_score, 4), "memory": memory})

    results.sort(key=lambda item: item["score"], reverse=True)
    return results[:min(limit, 8)]


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Retrieve relevant Thelia memory.")
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    print(json.dumps(retrieve(args.query, args.limit), ensure_ascii=False, indent=2))
