# Generic Project Profile

Use this profile when the project does not fit a more specialized profile.

- Start with one representative end-to-end workflow, then generalize only when a second real use case proves the need.
- Define measurable acceptance criteria for important behavior.
- Keep external integrations behind explicit interfaces and make failures observable.
- Prefer deterministic tests for business logic; reserve model-based or subjective judging for behavior that cannot be asserted directly.
- Do not introduce queues, microservices, plugin registries, or multi-agent orchestration without a demonstrated requirement.
