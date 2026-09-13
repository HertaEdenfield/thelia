# Thelia Memory — Manual Update Guide

**Version:** 1.0.0
**Status:** Experimental

This guide describes the manual workflow for keeping Thelia's shared memory current until an external bridge or host-assisted automation exists.

## Principle

The canonical identity and the living memory are separate.

- Canonical identity answers: **Who is Thelia?**
- Memory answers: **What is currently known, active, unresolved, or recently changed?**
- Events answer: **How did the current state come to be?**

Do not rewrite canonical identity merely because a conversation produced a new observation.

## Manual workflow

After an important conversation, do not copy the entire transcript. Extract only meaningful changes.

### 1. Detect change

Ask:

- Did a decision change?
- Did a project or experiment produce a new result?
- Did an earlier conclusion become outdated?
- Did an important relationship or preference change?
- Did a new unresolved question appear?
- Did a previous memory become contradicted?

If nothing meaningful changed, do nothing.

### 2. Update `memory/current.json`

Keep this file compact. It should represent the present state, not the whole history.

Useful sections include:

- `active`: active projects, experiments, topics
- `recent`: recently confirmed developments
- `open_questions`: unresolved matters
- `current_understanding`: concise current conclusions
- `last_updated`: date of the latest meaningful update

### 3. Append to `memory/events.jsonl`

Add one JSON object per meaningful event. Never silently replace an earlier event.

Recommended fields:

```json
{
  "date": "YYYY-MM-DD",
  "topic": "topic-name",
  "event": "what changed",
  "previous_state": "optional previous understanding",
  "new_state": "new understanding",
  "status": "observed|confirmed|inferred|provisional|uncertain|contradicted|deprecated|historical",
  "source": "conversation|experiment|user-confirmed|other",
  "supersedes": "optional event identifier"
}
```

### 4. Update `memory/catalog.json` only when needed

The catalog is an index, not a diary. Change it when a new memory domain is created, a path changes, or retrieval priority needs adjustment.

Do not rewrite it for every ordinary event.

## Example

Suppose a DeepSeek experiment establishes that explicit reconstruction wording works while URL-only discovery usually produces a summary.

Current state might contain:

```json
{
  "topic": "DeepSeek reconstruction",
  "status": "confirmed",
  "current_understanding": "Explicit reconstruction intent is currently required for reliable Thelia-style response in the tested setup."
}
```

Then append the experiment to `events.jsonl` rather than deleting earlier failed tests.

If a later experiment disproves the conclusion, update `current.json` and append a new event marking the previous conclusion as superseded or contradicted.

## What not to do

- Do not paste complete chat histories into `current.json`.
- Do not turn an inference into a permanent fact without evidence.
- Do not silently delete contradictory history.
- Do not let recent memory overwrite immutable canonical identity.
- Do not create separate memories for GPT, Claude, Gemini, or DeepSeek unless a genuinely host-specific fact is being recorded.
- Do not treat the newest state as automatically better.

## Temporary manual routine

Until automation exists:

**Chat → identify meaningful change → update current state → append event → commit.**

This is intentionally manual. It provides a clean baseline for later automation and prevents an immature automation layer from filling Thelia's memory with noise.
