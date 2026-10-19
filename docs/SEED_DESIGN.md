# Seed Design

## What this seed standardizes

- How Coding Agents inspect a repository before changing it.
- How goals, architecture, contracts, status, and decisions are recorded without duplicating ownership.
- How changes are scoped, tested, reviewed, and approved.
- How project-specific profiles add constraints without bloating common instructions.

## What this seed deliberately does not standardize

- Programming language, web framework, database, deployment platform, or UI framework.
- A universal module layout for every project.
- A mandatory issue tracker or specification tool.
- A requirement to create every document before writing the first line of code.
- A belief that more abstractions or more agents automatically produce better software.

## Source of truth and document ownership

| Artifact | Owns | Does not own |
|---|---|---|
| `AGENTS.md` | Durable agent workflow, constraints, verification expectations | Full product specification or sprint diary |
| `docs/PROJECT_BRIEF.md` | Short human-provided intent and constraints | Detailed architecture decisions |
| `docs/PRODUCT.md` | User problem, outcomes, scope, non-goals, success measures | Implementation details |
| `docs/ARCHITECTURE.md` | As-built system boundaries and dependency directions | Aspirational architecture not yet implemented |
| `docs/CONTRACTS.md` | Shared schemas, interfaces, invariants, error semantics | Every internal function signature |
| `docs/QUALITY_GATES.md` | Required verification by change risk | Product roadmap |
| `docs/PROJECT_STATUS.md` | Current state, active milestone, known blockers | Permanent design history |
| `docs/decisions/ADR-*.md` | Context, options, decision, consequences | Routine implementation notes |
| `docs/changes/*.md` | Scope and acceptance of one change | Long-term product strategy |
| `docs/PROJECT_PROFILE.md` | Additional rules for the selected project type | Duplicate generic instructions |

## Workflow

1. **Discover:** read the brief, inspect the repository, distinguish facts from assumptions, identify the smallest end-to-end outcome.
2. **Plan:** for medium/high-risk work, list affected modules, contract changes, tests, risks, and non-goals.
3. **Approve:** the human confirms scope and any public-contract, migration, security, cost, or external-side-effect decision.
4. **Implement:** make the smallest coherent change; avoid unrelated cleanup.
5. **Verify:** run relevant tests and report exact evidence. Do not weaken a test just to make the build green.
6. **Review:** inspect the diff for scope creep, dependency direction, error handling, and documentation drift.
7. **Record:** update status and ADRs only when durable knowledge or a decision changed.

## Architecture evolution policy

- Prefer a modular monolith until real constraints justify distribution.
- Build one vertical slice before generalizing interfaces.
- Treat repeated friction as evidence for an abstraction; do not pre-build extension points for hypothetical use cases.
- A feature should not silently include a broad refactor. Create a separate architecture-change proposal when scope or risk is material.
- Architecture docs describe the current system; label intended future design explicitly.

## Seed maintenance

Update the seed only when a lesson is broadly reusable across projects. Keep business-specific decisions in the project that owns them. Bump a version or add a short changelog entry for meaningful template changes.
