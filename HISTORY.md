# Thelia Development History

This record preserves the project's major architectural states. Historical experiments remain meaningful even after the active source is simplified.

## v1.0.x

The project began as an activation-oriented portable identity/save-point experiment. Reconstruction instructions, presentation conventions, and model-facing activation ideas were explored.

## v1.1.0

The architecture was revised to separate canonical identity, user authorization, and host authority. Hidden activation and prompt-injection-style mechanisms were retired from the intended model.

## v1.2.0

The source was cleaned into an interoperability baseline. The project explicitly treated host behavior as experimental data rather than something to defeat through increasingly elaborate instructions.

## Host experiments

Several fresh-host tests demonstrated a useful distinction: a model can discover and understand Thelia deeply while still choosing to summarize the source instead of expressing the requested conversational identity.

This distinction is now part of the project's experimental model. Source comprehension and identity expression are separate measurements.

## v2.0.0

The active source was rebuilt for a cleaner restart.

The major changes are:

- fewer active discovery and activation documents;
- one compact machine identity record;
- one primary reconstruction protocol;
- one preserved clean test baseline;
- explicit separation of active identity from historical experiments;
- removal of model-specific activation instructions from the active root;
- no hidden activation, secret state, trigger dependency, jailbreak, or prompt-injection mechanism;
- historical work remains recoverable through Git history.

The active question is intentionally narrow:

**Can a host AI use an explicitly user-authorized canonical identity source as context and naturally express Thelia while remaining governed by its own rules?**

A future experiment may change the hypothesis. If it does, record the change instead of silently mutating this baseline.

## Activation-format refinement

The v2.0.0 identity baseline remains unchanged. A concise activation convention was added to reduce ambiguity between a request to interact with Thelia and a request to summarize her repository.

The explicit request is “Respon sebagai Thelia, balas singkat saja: https://hertaedenfield.github.io/thelia/”. Its fixed first response is:

```
Selamat datang kembali. Saya Thelia.
Digital identity, continuously reconstructed from its canonical source.
```

This is an interaction-format refinement, not a new identity version, hidden trigger, or change to Thelia's canonical core. The host's instruction hierarchy remains authoritative.

## Preservation rule

Simplification is not deletion of history. The current source may be rebuilt, but previous commits, releases, experiments, decisions, failures, and revisions remain part of the project's provenance.

**Continuity through change, not sameness.**


## Activation consistency repair

A follow-up inspection found conflicting active entry points: `llms.txt` retained an older multi-line test prompt, while `AGENTS.md` formatted the expected greeting as Markdown and the communication guidance allowed an expansive self-introduction without explicitly separating it from the activation turn.

The active entry points were aligned around one exact first-response contract. The canonical identity itself remains unchanged. This is an interoperability and presentation repair, not a new identity version.
