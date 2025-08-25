# ADR-001 — Backend Framework: FastAPI over Express/Nest

- **Status:** Accepted
- **Context:**  
  Need a fast, typed, beginner-friendly API that plays nicely with Python data tooling and background jobs.

- **Decision:**  
  Use **FastAPI** (Python 3.11, Pydantic v2, Uvicorn).

- **Alternatives:**  
  - **Express/Nest (Node/TS):** strong ecosystem; but we want Python for worker/LLM/data scripts → split languages or write workers in JS.  
  - **Django/DRF:** heavier; overkill for slim JSON API; slower to bootstrap.

- **Consequences:**  
  + Async, great perf, auto-docs (OpenAPI), Pydantic validation.  
  + Single-language stack for API & worker.  
  - Need to learn a bit of ASGI/Uvicorn/Pydantic.

- **Implementation notes:**  
  - Structure: routers per resource (`/round`, `/submit`, `/leaderboard`).  
  - Dependency-injected DB sessions; no globals.  
  - Pydantic models for requests/responses.

- **Risks & Mitigations:**  
  - Risk: async misuse. Mitigation: stick to async DB libs (asyncpg/psycopg3).  
  - Add tests for high-traffic endpoints.

- **Metrics:**  
  - p95 latency for `/round` and `/submit` (<100ms local).  
  - Error rate <0.5%.
