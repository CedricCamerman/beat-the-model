'use client';

import { useEffect, useState } from 'react';

type Game = { id: string; display_name: string };

export default function Home() {
  const [games, setGames] = useState<Game[]>([]);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    const API = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000';
    fetch(`${API}/api/v1/games`)
      .then(r => r.json())
      .then(data => setGames(data.games))
      .catch(e => setErr(String(e)));
  }, []);

  return (
    <main>
      <h1>Beat The Model</h1>
      <p>Human vs AI skill games. (MVP scaffold)</p>
      <h2>Games</h2>
      {err && <pre style={{color:'crimson'}}>Error: {err}</pre>}
      <ul>
        {games.map(g => <li key={g.id}>{g.display_name} <small>({g.id})</small></li>)}
      </ul>
      {!games.length && !err && <p>Loading…</p>}
    </main>
  );
}
