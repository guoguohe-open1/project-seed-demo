# RAG / Knowledge-Augmented Generation Profile

Apply these rules in addition to the root `AGENTS.md`.

- Define the knowledge sources, ownership, freshness expectations, access controls, and deletion/update propagation before choosing a retrieval stack.
- Establish a representative evaluation set before tuning chunking, embeddings, rerankers, query rewriting, or context packing.
- Separate retrieval quality from generation quality. Track whether the required evidence was retrieved, whether it was used correctly, and whether the answer is supported.
- Preserve source identifiers and provenance through ingestion, retrieval, generation, and user-visible citations.
- Test stale facts, conflicting sources, missing evidence, access-control filtering, adversarial instructions inside retrieved content, and unanswerable questions.
- Compare a simple lexical baseline and a vector/hybrid baseline before adding agentic retrieval or complex multi-stage pipelines.
- Measure end-to-end quality, latency, cost, freshness, and permission correctness. Do not optimize retrieval metrics alone if final task success does not improve.
- Keep offline evaluation data separate from prompt/retrieval tuning data and document dataset limitations.
