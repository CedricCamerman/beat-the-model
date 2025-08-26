# Beat The Model: Human vs AI Benchmark (MVP)

Short, skill-based mini-games where humans compete **head-to-head** against **precomputed** LLM outputs.  
Focus: **low-latency**, **fair**, **cost-controlled** gameplay.

## Project Status

🚧 **This project is under active development.**  
The core scaffolding (Next.js + FastAPI + Postgres + Redis) is in place.  
Next milestone: implement `/api/v1/round` + `/api/v1/submit` for the first game loop.

## Stack

- **Web**: Next.js (TypeScript)
- **API**: FastAPI (Python 3.11, Uvicorn)
- **DB**: PostgreSQL 16 (with Alembic migrations)
- **Cache**: Redis 7
- **Worker**: Python (stub; for offline precompute)
- **Infra**: Docker + Docker Compose

## Why this architecture?

- **No live LLM calls on the hot path** → fast & cheap.
- **Redis** serves hot reads (rounds/leaderboards) in **<100ms**.
- **Server-only scoring** and **signed seeds** prevent tampering.
- **Postgres** stores rounds, results, and ELO ratings reliably.

## Prerequisites

- Docker Desktop (Win/macOS) or Docker Engine (Linux)
- Git
- (Optional) Node 20+ locally (not required if you run via Docker)

## Quickstart (first run)

```bash
# 1) Build images
docker compose build

# 2) Start DB + Redis
docker compose up -d db cache

# 3) Create tables
docker compose run --rm api alembic upgrade head

# 4) Start API, Worker, Web
docker compose up -d api worker web

# 5) Verify
curl http://localhost:8000/health   # -> {"ok": true}
```

## Architecture Diagrams

- [System Context (C4)](docs/uml/src/c4-system-context.mmd)  
- [Sequence: Play Round](docs/uml/src/play-round-sequence.mmd)  
- [Entity Relationship (ERD)](docs/uml/src/erd.mmd)
