# ADR-007 — Ratings: Elo over Glicko

- **Status:** Accepted
- **Context:**  
  Need a simple, understandable rating with minimal math/state.

- **Decision:**  
  Use **Elo** with fixed K (e.g., 24), per game + overall.

- **Alternatives:**  
  - Glicko/Glicko-2: better uncertainty, but more params.  
  - Simple cumulative score: no opponent strength modeling.

- **Consequences:**  
  + Easy to implement, easy to explain.  
  - No uncertainty tracking.

- **Implementation notes:**  
  - Treat “AI opponent” as fixed rating per difficulty (e.g., 1500/1700/1900).  
  - Update per submitted round or per session.

- **Risks & Mitigations:**  
  - Rating inflation. Mitigation: cap K; seasonal resets.

- **Metrics:**  
  - Rating distribution bell-shaped.  
  - User movement feels fair.
