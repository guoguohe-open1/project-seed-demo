# Agent Application Profile

Apply these rules in addition to the root `AGENTS.md`.

- Define the Agent's authority: which actions are read-only, reversible, sensitive, or prohibited.
- Enforce authorization in application code at each tool/action boundary; prompts are not an access-control mechanism.
- Validate tool inputs and outputs against explicit schemas. Treat retrieved documents, user text, and tool results as untrusted data.
- Define timeouts, retry limits, idempotency behavior, and compensation for side-effecting actions.
- Keep task state explicit. For long-running workflows, decide how checkpointing, interruption, resume, and human approval work before implementing them.
- Capture trace IDs, tool inputs/outputs (with appropriate redaction), latency, failures, and model usage.
- Evaluate complete task outcomes, not only answer quality. Include ambiguity, tool failure, prompt injection, and permission-denial scenarios.
- Start with a single-agent workflow unless experiments demonstrate a benefit from multi-agent coordination.
