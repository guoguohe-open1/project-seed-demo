# Quality Gates

Use risk-based gates. The goal is reliable feedback, not paperwork for every edit.

## Gate 0 — Scope
Before implementation, identify the user-visible outcome, acceptance criteria, non-goals, and any unresolved assumptions. Small low-risk changes may do this in the task description; medium/high-risk changes need a written spec.

## Gate 1 — Impact analysis
For cross-module or risky changes, list affected modules, public contracts, data formats, callers, security boundaries, dependencies, and recovery needs. If a public contract or architecture decision changes, update the relevant document and consider an ADR.

## Gate 2 — Implementation
- Make the smallest coherent change.
- Add tests for new behavior and important failure paths.
- Preserve unrelated changes and avoid opportunistic refactors.
- Do not change the benchmark or weaken assertions to make results look better.

## Gate 3 — Verification
Run checks appropriate to the repository and change:
- formatting / lint / type checks, if configured;
- unit tests for local logic;
- contract and integration tests for boundary behavior;
- regression / golden tests for user-visible behavior;
- security, permission, retry, recovery, and negative-path tests when relevant.

Report exact commands and outcomes. Clearly mark checks that were not run or were blocked.

## Gate 4 — Diff and documentation review
- Does the diff match the approved scope?
- Are there hidden interface changes, duplicated logic, new dependencies, or circular imports?
- Are errors, retries, timeouts, and side effects handled intentionally?
- Do docs describe actual behavior rather than aspirations?
- Can another developer reproduce the verification?

## Gate 5 — Human approval
Explicit approval is required for destructive migrations, production changes, external writes, permission changes, material dependency changes, and broad architecture rewrites.

## Minimum evidence in completion report
1. Summary of behavior changed.
2. Files / contracts changed.
3. Tests and checks actually run, with results.
4. Known limitations, risks, and checks not run.
5. Any decision required from the human.
