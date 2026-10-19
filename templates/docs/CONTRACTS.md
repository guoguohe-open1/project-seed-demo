# Contracts and Invariants

Record only contracts shared across module boundaries or needed to preserve correctness. Keep local implementation details in code.

## Domain terms
| Term | Meaning | Canonical representation |
|---|---|---|
| TBD | TBD | TBD |

## Shared schemas and interfaces
- Name / location: TBD
- Required fields and validation: TBD
- Compatibility / versioning policy: TBD
- Error representation: TBD

## Invariants
- TBD — state conditions that must always remain true.

## Side-effect rules
- Authorization is checked by deterministic code at the action boundary.
- Retried operations must define whether they are idempotent or how duplicates are detected.
- Read-only evaluation and grading paths must not mutate the system under test unless explicitly specified.

## Compatibility and migrations
- Backward compatibility expectations: TBD
- Migration owner and rollback approach: TBD

## Contract tests
- TBD — link to tests that enforce the important contracts.
