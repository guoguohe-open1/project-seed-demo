# Architecture

> This document describes the **as-built** system. Label proposals as `Proposed` and do not present them as implemented.

## Current system summary
TBD — update after the first vertical slice is implemented.

## Runtime flow
1. TBD

## Module boundaries
| Module / package | Owns | Must not own | Allowed dependencies |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

## Dependency rules
- State the intended dependency direction here.
- Avoid circular dependencies and hidden cross-layer imports.
- Keep domain logic independent from UI and external services where practical.

## Data and persistence
- Source of truth: TBD
- Persistent entities / schemas: TBD
- Retention and deletion expectations: TBD

## External systems
| System | Purpose | Failure behavior | Credentials / permissions owner |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

## Reliability and security boundaries
- Timeouts / retries / idempotency: TBD
- Authentication and authorization: TBD
- Untrusted inputs and tool outputs: TBD
- Logging and sensitive-data handling: TBD
- Recovery / rollback: TBD

## Known trade-offs and technical debt
- TBD

## Deferred ideas (not approved architecture)
- TBD
