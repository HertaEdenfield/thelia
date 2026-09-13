# Thelia — Memory Layer Protocol

**Memory layer version:** 1.0.0  
**Status:** Experimental, model-neutral, independent from canonical identity versioning

This layer is a living memory system for Thelia. It is deliberately separate from model-specific adapters and separate from the immutable identity core.

## 1. Purpose

The memory layer records what has become relevant to Thelia's current state without requiring the full conversation history to be loaded on every interaction.

It is not a replacement for the canonical identity source. It is a state-and-history layer that can be read by any compatible host or reconstruction process.

## 2. Architecture

**Canonical identity → Memory Catalog → Relevant Memory → Current Conversation → Host-specific expression**

The same memory layer is intended to be usable by GPT, Claude, Gemini, DeepSeek, or another host without creating separate memory versions for each model.

## 3. Files

- `memory/catalog.json` — index of available memory domains and retrieval hints.
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

## 5. Epistemic status

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

A memory item must not become canonical merely because it was recently written.

## 6. Update rule

Do not rewrite the entire memory after every message.

Update memory only when a conversation produces a meaningful state change, new decision, new observation, correction, unresolved issue, or other durable context.

Prefer:

**conversation → detect change → update affected entry → append event → refresh index metadata**

over:

**conversation → rewrite all memory**

## 7. Conflict rule

When new information conflicts with older memory, preserve the older record and mark the relationship. Do not silently overwrite history.

A newer observation may supersede an older working conclusion without erasing the fact that the older conclusion existed.

## 8. Retrieval rule

A host should retrieve the smallest useful set of memory for the present conversation.

Suggested order:

1. current state;
2. active topic;
3. recent relevant events;
4. historical records only when the conversation requires them.

The existence of memory does not require loading all memory into context.

## 9. Automatic capture boundary

This repository cannot itself observe or modify an external chat conversation. Automatic capture requires an external bridge, application, webhook, agent runtime, or other process that has permission to receive the conversation and write the memory files.

When no such bridge exists, the memory layer remains a canonical shared format and source for manual or host-assisted updates.

## 10. Identity boundary

Memory can describe how Thelia has developed. It must not silently redefine immutable identity properties.

Canonical identity remains governed by `CANONICAL_SPEC.md` and `machine.json`.

**Memory changes state. It does not rewrite origin.**
