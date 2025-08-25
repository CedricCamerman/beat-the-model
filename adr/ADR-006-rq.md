# ADR-006 — Background Jobs: RQ (Redis Queue) over Celery

- **Status:** Accepted (MVP)
- **Context:**  
  Need a lightweight Python job runner to batch LLM calls and schedule refreshes.

- **Decision:**  
  Use **RQ** with Redis (already in stack) for simplicity.

- **Alternatives:**  
  - Celery: more features, but more config.  
  - Cron + scripts: simplest, but no retry/visibility.

- **Consequences:**  
  + Minimal setup; leverages Redis; easy retries.  
  - Fewer advanced features than Celery.

- **Implementation notes:**  
  - One `worker` service runs an RQ worker.  
  - A tiny scheduler enqueues periodic jobs.

- **Risks & Mitigations:**  
  - Job loss on crashes. Mitigation: idempotent jobs; re-enqueue on startup.

- **Metrics:**  
  - Job success rate > 99%.  
  - Average precompute throughput OK.
