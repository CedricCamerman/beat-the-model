# ADR-005 — Packaging: Monorepo + Docker Compose (dev) + Simple PaaS (prod)

- **Status:** Accepted
- **Context:**  
  Solo project; want a single repo and one command to run everything.

- **Decision:**  
  Monorepo with `web/`, `api/`, `worker/` and `compose.yml`. Deploy to Vercel (web) + Fly/Render (api/worker) initially.

- **Alternatives:**  
  - Polyrepo: more isolation but heavier DX.  
  - Full Kubernetes: overkill for MVP.

- **Consequences:**  
  + Fast local dev; consistent tooling; easier refactors.  
  - Repo grows larger; requires structure discipline.

- **Implementation notes:**  
  - One `.env.example`, consistent lint/test scripts.  
  - Volumes for hot-reload in dev.

- **Risks & Mitigations:**  
  - Compose drift. Mitigation: document boundaries; keep infra in `/infra`.

- **Metrics:**  
  - Time-to-first-run < 30 min from clone.  
  - “One command up” works.
