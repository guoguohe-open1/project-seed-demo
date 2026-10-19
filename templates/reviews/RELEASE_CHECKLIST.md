# Release / Milestone Checklist

## Scope and evidence
- [ ] Acceptance criteria are met with observed evidence.
- [ ] Changes match the approved scope; unrelated changes are removed or separately tracked.
- [ ] Known limitations and unverified areas are documented.

## Quality
- [ ] Relevant unit, contract, integration, and regression tests passed, or deviations are explicitly accepted.
- [ ] Error handling and negative paths were checked where relevant.
- [ ] No secrets, private user data, or unintended debug artifacts are included.
- [ ] Dependency and configuration changes are intentional.

## Operability and safety
- [ ] Logging and metrics are adequate for the changed behavior.
- [ ] Permissions and external side effects are constrained.
- [ ] Migration, rollback, or recovery is understood if applicable.

## Documentation and decision
- [ ] User-facing documentation and contracts reflect the actual behavior.
- [ ] ADR / project status updated if a durable decision or milestone changed.
- [ ] Human approval obtained for required high-risk actions.
