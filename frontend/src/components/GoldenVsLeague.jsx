import React, { useEffect, useState } from "react";

const GoldenVsLeague = () => {
  const [result, setResult] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/golden-vs-league", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        golden_path: "dummy",
        session_path: "dummy"
      })
    })
      .then(res => res.json())
      .then(data => setResult(data));
  }, []);

  if (!result) return <div>Loading Golden vs. League...</div>;

  return (
    <div style={{ marginTop: "2rem", padding: "1rem", border: "1px solid #ccc", borderRadius: "8px" }}>
      <h2>🏅 Golden vs. League</h2>
      <p><strong>Score Difference:</strong> {result.score_diff}</p>
      <p><strong>Notes:</strong> {result.notes}</p>
    </div>
  );
};

export default GoldenVsLeague;
