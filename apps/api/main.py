from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
import redis

DATABASE_URL = os.environ["DATABASE_URL"]
REDIS_URL = os.environ["REDIS_URL"]

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
r = redis.from_url(REDIS_URL, decode_responses=True)

app = FastAPI(title="Beat The Model API", version="0.1.0")

# CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health(db: Session = Depends(get_db)):
    # simple DB & Redis check
    try:
        db.execute(text("SELECT 1"))
        r.ping()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"ok": True}

# --- simple data access ---

@app.get("/api/v1/games")
def list_games(db: Session = Depends(get_db)):
    rows = db.execute(text("SELECT id, display_name FROM games ORDER BY id")).mappings().all()
    return {"games": [dict(r) for r in rows]}
