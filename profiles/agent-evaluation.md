# Agent Evaluation & Simulation Profile

Apply these rules in addition to the root `AGENTS.md`.

## Core entities to consider
- **Scenario / EvaluationCase:** task goal, initial state, permitted actions, constraints, and success criteria.
- **Run:** one execution with versions, inputs, trace, timing, token/cost data, and final state.
- **Trace:** ordered model steps, tool calls, tool results, and relevant state transitions.
- **Grader / EvaluationResult:** verdict, evidence, failure category, and grader version.

Do not implement every entity up front; validate the smallest schema that supports the first end-to-end evaluation.

## Evaluation invariants
- The grader must use observable evidence. For stateful tasks, verify final environment state rather than trusting the Agent's self-report.
- Grading should be read-only with respect to the system under test.
- Each run must have an isolated or reproducibly resettable environment.
- Store scenario version, Agent/model/prompt version, environment version, and grader version with results.
- Separate development / tuning data from held-out evaluation data to reduce benchmark overfitting.
- Report failures and uncertainty honestly. Do not collapse infrastructure failures into Agent failures without labeling them.
- Repeated runs may be necessary for stochastic systems; define and report the aggregation method.

## Important failure categories
- Intent / goal misunderstanding
- Missing clarification or incorrect assumption
- Wrong tool or malformed arguments
- Business-rule violation
- Incorrect state transition
- Tool/environment failure
- Recovery / retry failure
- Permission or safety violation
- Correct action but incorrect user communication
- Grader ambiguity or infrastructure error

## Suggested first vertical slice
One scenario → reset environment → execute one Agent → capture trace and final state → run deterministic grader → emit a reproducible result. Add UI, distributed workers, and automatic optimization only after this loop is trustworthy.

## Metrics to consider
Task success rate, policy-violation rate, tool-call correctness, repeatability (for example pass^k), latency percentiles, token / monetary cost per successful task, grader agreement, and failure-category distribution. Select only metrics relevant to the product.
