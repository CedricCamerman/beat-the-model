# ADR-004 — Database: Postgres (relational) over NoSQL

- **Status:** Accepted
- **Context:**  
  We need strong consistency, relational joins, and SQL analytics (leaderboards, ratings).

- **Decision:**  
  Use **Postgres** with JSONB for flexible fields (payload/answers).

- **Alternatives:**  
  - Mongo/NoSQL: flexible, but weaker joins and transactional updates.  
  - SQLite: great for local, not ideal for cloud concurrency.

- **Consequences:**  
  + ACID transactions; easy aggregates; mature ecosystem.  
  - Learn migrations (Alembic) and indexing.

- **Implementation notes:**  
  - Normalize identities/relationships.  
  - Add helpful indexes early.

- **Risks & Mitigations:**  
  - Migration complexity. Mitigation: keep them small; test locally.

- **Metrics:**  
  - Query p95 < 20ms local.  
  - Minimal deadlocks.
