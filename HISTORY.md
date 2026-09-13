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

## Preservation rule

Simplification is not deletion of history. The current source may be rebuilt, but previous commits, releases, experiments, decisions, failures, and revisions remain part of the project's provenance.

**Continuity through change, not sameness.**
