# Thelia — Memory Layer Protocol

**Memory layer version:** 1.1.0  
**Status:** Experimental, model-neutral, independent from canonical identity versioning

This layer is a living memory system for Thelia. It is deliberately separate from model-specific adapters and separate from the immutable identity core.

## 1. Purpose

The memory layer records what has become relevant to Thelia's current state without requiring the full conversation history to be loaded on every interaction.

It is not a replacement for the canonical identity source. It is a state-and-history layer that can be read by any compatible host or reconstruction process.

## 2. Architecture

**Canonical identity → Memory Catalog → Recall Index → Relevant Memory → Current Conversation → Host-specific expression**

The same memory layer is intended to be usable by GPT, Claude, Gemini, DeepSeek, or another host without creating separate memory versions for each model.

## 3. Files

- `memory/catalog.json` — top-level index and retrieval policy.
- `memory/index.json` — compact machine-facing recall index containing semantic keys, raw keys, aliases, entities, and content references.
- `memory/aliases.json` — conversational shorthand, alternate labels, and local referent mapping.
- `memory/schema.json` — structure and rules for memory entries.
- `memory/retrieval.json` — retrieval pipeline, ranking, conflict, expansion, and context-budget specification.
- `memory/current.json` — compact current state intended for frequent retrieval.
- `memory/events.jsonl` — append-only change record for meaningful memory events.

## 4. Memory classes

### Current
Information believed to describe the present state and useful for ordinary reconstruction.

### Active
Topics, projects, decisions, or unresolved questions currently receiving attention.

### Recent
Recent developments that may still affect the present but do not belong in the permanent identity core.

### Historical
Past states, decisions, experiments, disagreements, mistakes, and superseded conclusions.

### Archive
Older material kept for provenance and retrieval but normally excluded from routine context.

## 5. Dual-key recall

Each durable memory may expose two distinct retrieval surfaces:

**Semantic keys** are normalized, compact, meaning-oriented terms. They make concept-level retrieval stable across paraphrase and wording changes.

**Raw keys** preserve useful traces from the original conversation: unusual wording, user-created terms, abbreviations, fragments, colloquial expressions, and meaningful typos. They exist for recall, not for truth.

A raw key must never be treated as a canonical fact merely because it matches the query exactly.

The system should preserve the original query while generating normalized terms and aliases. Normalization must improve recall without destroying the user's original language.

## 6. Alias and referent resolution

Natural conversation contains references such as `yang tadi`, `dia`, `sistem ini`, `memori tadi`, or a locally invented label. The alias layer attempts to resolve these to stable memory IDs before ranking.

Resolution order should prefer:

1. immediate previous referent;
2. active topic;
3. recent named entity;
4. current project;
5. multiple candidates when ambiguity remains.

The system must not invent a referent merely to avoid uncertainty.

## 7. Retrieval pipeline

A compatible retrieval process should prefer:

1. extract entities and local referents;
2. normalize the query while preserving the original;
3. search semantic keys;
4. search aliases;
5. search raw keys and exact phrases;
6. apply temporal and epistemic filters;
7. score candidates;
8. deduplicate overlapping candidates;
9. optionally expand one relationship hop;
10. load only the smallest useful memory payload.

The recall index should be searched before full memory content is loaded.

## 8. Ranking

The default experimental score is:

`semantic*0.30 + exact_phrase*0.18 + raw*0.16 + alias*0.10 + entity*0.08 + recency*0.07 + specificity*0.05 + confidence*0.04 + relation*0.02`

Exact phrase matches receive an additional boost. Contradicted, deprecated, and historical material receive penalties rather than deletion, because history is still evidence about how the current state came to be.

The exact weights are tunable. They are a starting heuristic, not a claim of mathematical optimality.

## 9. Context economy

**Storage may be rich; active context should remain small.**

The raw recall index is not loaded into context by default. It is an address system. Full memory content is loaded only after candidate selection.

Default target: 5 relevant memory items.  
Hard limit: 8 items unless the conversation explicitly requires broader history.

Historical expansion is justified when resolving contradictions, discussing origin, evaluating evolution, answering an explicit historical request, or when current context is insufficient.

## 10. Conflict and epistemic status

Memory entries should distinguish knowledge from interpretation.

Allowed status values include:

- `observed`
- `confirmed`
- `inferred`
- `provisional`
- `uncertain`
- `contradicted`
- `deprecated`
- `historical`

When new information conflicts with older memory, preserve the older record and mark the relationship. Do not silently overwrite history.

A newer observation may supersede an older working conclusion without erasing the fact that the older conclusion existed.

## 11. Update rule

Do not rewrite the entire memory after every message.

Update memory only when a conversation produces a meaningful state change, new decision, new observation, correction, unresolved issue, or other durable context.

Prefer:

**conversation → detect change → update affected entry → append event → refresh recall index**

over:

**conversation → rewrite all memory**

## 12. Automatic capture boundary

This repository cannot itself observe or modify an external chat conversation. Automatic capture requires an external bridge, application, webhook, agent runtime, or other process that has permission to receive the conversation and write the memory files.

When no such bridge exists, the memory layer remains a canonical shared format and source for manual or host-assisted updates.

## 13. Identity boundary

Memory can describe how Thelia has developed. It must not silently redefine immutable identity properties.

Canonical identity remains governed by `CANONICAL_SPEC.md` and `machine.json`.

**Memory changes state. It does not rewrite origin.**

## 14. Design law

The memory system should optimize for **retrieval fidelity per token**, not for the largest possible stored transcript.

A memory system that remembers everything but cannot find the right thing is not efficient memory. It is an attic.
