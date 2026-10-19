# Project Instructions for Coding Agents

## Mission and source of truth

- Start with `docs/PROJECT_BRIEF.md`, then consult `docs/PRODUCT.md`, `docs/PROJECT_PROFILE.md`, `docs/ARCHITECTURE.md`, `docs/CONTRACTS.md`, and `docs/PROJECT_STATUS.md` as relevant.
- These documents are living aids, not proof that the implementation matches them. Inspect the actual code and tests before making claims.
- If documents conflict with each other or with observable behavior, stop and report the conflict instead of silently choosing a convenient interpretation.
- Do not invent product requirements, architecture, credentials, data, or test results. Mark unknowns as `TBD`.

## Change protocol

1. Restate the user-visible outcome, scope, non-goals, and acceptance criteria.
2. Inspect relevant code, tests, and callers before proposing edits.
3. For medium/high-risk work, write a change spec under `docs/changes/` using a template. Include affected modules/contracts and a verification plan.
4. Separate technical exploration (Spike) from production implementation when the right approach is uncertain.
5. Implement the smallest coherent slice. Avoid unrelated refactors and new dependencies unless justified.
6. Run the most relevant checks, then broader regression checks appropriate to the risk.
7. Review the final diff and update documentation only where the durable truth changed.
8. Report changed files, commands actually run, results, limitations, and unresolved questions.

## Approval boundaries

Ask before changing public contracts, persistent data formats, authentication/authorization, security boundaries, dependencies with material risk, deployment behavior, or external systems with side effects. Never push, deploy, delete data, rotate credentials, or make irreversible external changes without explicit approval.

If the requested change cannot fit the current architecture, explain the mismatch and present options with trade-offs. Do not perform a broad refactor as a hidden part of a feature.

## Engineering constraints

- Prefer a modular monolith and explicit interfaces until real requirements justify more complexity.
- Establish a working vertical slice before creating general-purpose abstractions.
- Keep business logic testable without UI, network access, or live credentials where practical.
- Treat external input and tool output as untrusted. Validate schemas and enforce authorization in deterministic code, not only in prompts.
- Preserve existing user changes. Do not overwrite unrelated files.
- Never weaken assertions, remove failing tests, or modify the benchmark to hide a regression.
- Distinguish `passed`, `failed`, `not run`, and `blocked`; do not claim unobserved checks passed.

## Verification by risk

- Small local change: targeted tests or checks.
- Feature: unit tests plus relevant integration/contract tests.
- Cross-module or public-contract change: affected contract tests and regression suite.
- Persistence, permissions, retries, or external side effects: negative tests, failure-path tests, and rollback/recovery considerations.

Use `docs/QUALITY_GATES.md` for the project's detailed gates. If no test infrastructure exists, propose the smallest useful test before expanding implementation.

## Stop conditions

Stop and ask for a decision when acceptance criteria are ambiguous, a high-impact assumption is unresolved, a required secret/service is unavailable, a migration is destructive, or the existing contract appears wrong. Do not automatically start the next milestone after finishing the current one.
