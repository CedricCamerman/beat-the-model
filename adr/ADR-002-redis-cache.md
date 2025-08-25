# ADR-002 — Cache Layer: Redis (L1) + Postgres (source of truth)

- **Status:** Accepted
- **Context:**  
  Hot endpoints must be sub-100ms; DB alone may be too slow under bursty read.

- **Decision:**  
  Use **Redis** for hot reads (round payloads, Elo, top-N) with **Postgres** as authoritative storage.

- **Alternatives:**  
  - No cache: simplest, but higher latency and DB load.  
  - In-process cache: dies on restart; not shareable across replicas.

- **Consequences:**  
  + Very low latency for hot keys.  
  + Elastic scaling (API replicas share cache).  
  - Extra moving part; need eviction/TTL strategy.

- **Implementation notes:**  
  - Keys: `round:{game}:{seed}:{diff}`, `elo:{user}:{game}`, `lb:daily:{game}`.  
  - Warm cache during precompute; set TTLs as needed.

- **Risks & Mitigations:**  
  - Stale data: keep round content immutable; rebuild cache nightly.

- **Metrics:**  
  - Redis hit-rate >85% for `/round`.  
  - API p95 latency.
