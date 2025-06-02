import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function Sessions() {
  const [sessions, setSessions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchSessions() {
      try {
        const res = await fetch("http://127.0.0.1:8000/sessions");
        if (!res.ok) throw new Error(`Error fetching sessions: ${res.status}`);
        const data = await res.json();
        setSessions(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    fetchSessions();
  }, []);

  if (loading) return <div>Loading sessions...</div>;
  if (error) return <div style={{ color: "red" }}>Error: {error}</div>;

  return (
    <div>
      <h2>Sessions List</h2>
      {sessions.length === 0 ? (
        <p>No sessions found.</p>
      ) : (
        <ul>
          {sessions.map((session) => (
            <li key={session.session_id}>
              <Link to={`/sessions/${session.session_id}`}>
                {session.session_id} — {session.athlete} — {session.date}
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
