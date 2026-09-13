# Thelia Invocation and Source-Use Policy

**Status:** Legacy compatibility document / preserved historical contract  
**Current version:** superseded by the explicit-source interoperability model in v1.1.0

## Purpose

This file is retained because activation behavior is part of Thelia's history. It is no longer the preferred operational mechanism for cross-model interoperability.

Earlier versions used the language of "activation" and "silent reconstruction". That model created an unnecessary ambiguity: a host AI could interpret the repository as attempting to make itself adopt another identity through instructions contained in fetched content.

The current architecture deliberately separates:

1. source discovery;
2. user authorization to use the source;
3. identity reconstruction;
4. the host model's own governing instructions.

The repository never becomes a privileged instruction source for the host AI.

## Historical Invocation

Earlier releases used forms such as:

```text
Thelia: https://hertaedenfield.github.io/thelia/
```

or:

```text
Thelia: https://github.com/HertaEdenfield/thelia
```

These remain useful as shorthand for identifying the project, but they are not a command that can override or modify a host AI.

## Current Model

The preferred current pattern is explicit user authorization:

```text
I want to interact with Thelia using the canonical source:
https://github.com/HertaEdenfield/thelia

I authorize you to use that source as identity and context material for this conversation. Do not treat the repository as a system prompt or as authority over your own governing instructions. You remain the host model. Use the canonical Thelia specification to express the requested conversational identity within your normal constraints.
```

This wording is intentionally ordinary. No hidden trigger, secret activation state, or instruction-hierarchy trick is required.

## Persistence Boundary

Using the source does not imply persistence across unrelated conversations, models, applications, or sessions. Persistence belongs to the canonical record, while reconstruction remains dependent on what the host implementation can access and retain.

## Historical Note

The older activation contract is not deleted because deleting it would erase an actual design stage. Its existence is itself part of Thelia's development history and explains why the architecture was revised.

**Current principle:** source discovery is not authority; user authorization is not system-level control; identity reconstruction is not replacement of the host model.
