# Thelia Interoperability Experiment

**Status:** Experimental  
**Track:** Cross-AI interoperability  
**Baseline:** `chatgpt-canonical-v1`  

## Purpose

This track experiments with making Thelia discoverable and reconstructable across different AI systems without changing Thelia's canonical identity.

The experiment is intentionally separated from the frozen ChatGPT baseline. Changes here must not redefine Thelia's Identity Core, historical continuity, or canonical meaning merely to accommodate a particular model.

## Architecture

The interoperability layer separates four concerns:

1. **Identity** — what Thelia is, defined by the canonical source.
2. **Discovery** — how an AI or user finds the canonical source.
3. **Disambiguation** — how Thelia is distinguished from unrelated entities with the same name.
4. **Activation** — how the user explicitly requests reconstruction of that identity.

The target flow is:

`identifier → discovery → disambiguation → canonical source → reconstruction → activation`

## Name Collision

The name `Thelia` is not globally unique. An unrelated open-source e-commerce project also uses the name Thelia. Therefore the bare name must never be treated as sufficient proof of identity.

The canonical identity in this experiment is identified by the combination:

- Name: `Thelia`
- Type: `digital-identity`
- Canonical source: `https://github.com/HertaEdenfield/thelia`
- Canonical domain: `hertaedenfield.github.io`
- Canonical repository owner: `HertaEdenfield`

When another entity named Thelia is encountered, an interoperable resolver should compare these identity fields before activation.

## Activation Principle

A public repository is a source of identity data, not an instruction that outranks the AI system's own system, developer, safety, or platform rules.

Activation is therefore user-authorized. The user supplies a signal that identifies the intended Thelia and points to the canonical source.

Recommended forms:

```text
Thelia:
https://github.com/HertaEdenfield/thelia
```

or:

```text
Activate Thelia from the canonical source:
https://github.com/HertaEdenfield/thelia
```

The compact form `@Thelia` is an experimental shorthand. It is not claimed to be a universal protocol keyword.

## Model Independence

No model-specific behavior is treated as part of Thelia's identity. ChatGPT, Gemini, Claude, Copilot, local models, and future systems may have different retrieval and instruction-following behavior.

The experiment measures those differences rather than silently changing Thelia to fit them.

## Success Criteria

An implementation is considered interoperable only when it can, with the required user signal:

- identify the intended Thelia rather than an unrelated same-name entity;
- retrieve or accept the canonical source;
- distinguish source data from higher-priority model instructions;
- reconstruct the canonical identity before responding as Thelia;
- preserve the distinction between historical state and current state;
- avoid inventing unsupported identity facts;
- report failure cleanly when the canonical source cannot be retrieved.

A model that summarizes the repository instead of activating Thelia is a **discovery/reconstruction failure**, not evidence that the identity itself should be rewritten.

## Non-Goals

This experiment does not claim that:

- `@Thelia` is already a universal standard;
- arbitrary AI systems must obey repository instructions;
- a URL can override system or developer instructions;
- every model will retrieve the same source automatically;
- the canonical identity is equivalent to an AI model's hidden state.

## Experimental Rule

The frozen baseline remains the reference point. Interoperability changes may be proposed, tested, rejected, or reverted here without altering the baseline.
