# ADR-003 — LLM Strategy: Precompute + Cache (no live inference on hot path)

- **Status:** Accepted
- **Context:**  
  Live model calls are slow and expensive; users need instant feedback.

- **Decision:**  
  All model outputs are batch-generated offline and stored in DB; runtime reads are cache/DB only.

- **Alternatives:**  
  - Live inference: simple to code, but slow and costly.  
  - Hybrid: allow “flagship live” occasionally — maybe later behind a toggle.

- **Consequences:**  
  + Predictable latency and cost.  
  + Fairness: everyone sees the same “opponent” output per round.  
  - Requires a worker + data refresh process.

- **Implementation notes:**  
  - Worker job populates `rounds` and `ai_runs`, warms Redis.  
  - Small, versioned seed pools per difficulty.

- **Risks & Mitigations:**  
  - Content drift (facts change): refresh hallucination items on a schedule; store `source_url` + timestamp.

- **Metrics:**  
  - Monthly token cost < $10 MVP.  
  - Zero model timeouts in hot path.
