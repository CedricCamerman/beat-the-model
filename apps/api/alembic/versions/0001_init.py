"""init schema
Revision ID: 0001_init
Revises:
Create Date: 2025-08-21
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = '0001_init'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.execute("""
    CREATE EXTENSION IF NOT EXISTS pgcrypto;
    """)
    op.execute("""
    CREATE TABLE IF NOT EXISTS users (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      handle TEXT UNIQUE,
      created_at TIMESTAMPTZ DEFAULT now()
    );
    """)
    op.execute("""
    CREATE TABLE IF NOT EXISTS games (
      id TEXT PRIMARY KEY,
      display_name TEXT NOT NULL
    );
    """)
    op.execute("""
    CREATE TABLE IF NOT EXISTS rounds (
      id BIGSERIAL PRIMARY KEY,
      game_id TEXT REFERENCES games(id),
      seed TEXT NOT NULL,
      difficulty INT NOT NULL DEFAULT 1,
      payload JSONB NOT NULL,
      answer_key JSONB NOT NULL,
      ai_meta JSONB NOT NULL,
      created_at TIMESTAMPTZ DEFAULT now(),
      UNIQUE(game_id, seed, difficulty)
    );
    """)
    op.execute("""
    CREATE TABLE IF NOT EXISTS ai_runs (
      id BIGSERIAL PRIMARY KEY,
      round_id BIGINT REFERENCES rounds(id) ON DELETE CASCADE,
      model TEXT NOT NULL,
      temperature REAL,
      prompt_hash TEXT NOT NULL,
      output JSONB NOT NULL,
      created_at TIMESTAMPTZ DEFAULT now()
    );
    """)
    op.execute("""
    CREATE TABLE IF NOT EXISTS results (
      id BIGSERIAL PRIMARY KEY,
      user_id UUID REFERENCES users(id),
      round_id BIGINT REFERENCES rounds(id),
      game_id TEXT NOT NULL,
      seed TEXT NOT NULL,
      difficulty INT NOT NULL,
      user_answer JSONB NOT NULL,
      outcome TEXT NOT NULL,
      score INT NOT NULL,
      time_ms INT,
      created_at TIMESTAMPTZ DEFAULT now()
    );
    """)
    op.execute("""
    CREATE TABLE IF NOT EXISTS ratings (
      user_id UUID REFERENCES users(id),
      game_id TEXT,
      rating INT NOT NULL DEFAULT 1200,
      rd REAL NOT NULL DEFAULT 350,
      updated_at TIMESTAMPTZ DEFAULT now(),
      PRIMARY KEY (user_id, game_id)
    );
    """)
    op.execute("""
    CREATE TABLE IF NOT EXISTS leaderboard_snapshots (
      id BIGSERIAL PRIMARY KEY,
      scope TEXT NOT NULL,
      payload JSONB NOT NULL,
      created_at TIMESTAMPTZ DEFAULT now()
    );
    """)
    # seed games
    op.execute("""
      INSERT INTO games (id, display_name) VALUES
      ('next_token','Next-Token Duel'),
      ('hallucination','Hallucination Hunter'),
      ('constraint','Constraint Solver')
      ON CONFLICT (id) DO NOTHING;
    """)

def downgrade():
    op.execute("DROP TABLE IF EXISTS leaderboard_snapshots;")
    op.execute("DROP TABLE IF EXISTS ratings;")
    op.execute("DROP TABLE IF EXISTS results;")
    op.execute("DROP TABLE IF EXISTS ai_runs;")
    op.execute("DROP TABLE IF EXISTS rounds;")
    op.execute("DROP TABLE IF EXISTS games;")
    op.execute("DROP TABLE IF EXISTS users;")
