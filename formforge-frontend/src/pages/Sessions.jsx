import { useEffect, useState } from "react";

export default function Sessions() {
  const [sessions, setSessions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchSessions() {
      setLoading(true);
      setError("");
      try {
        const res = await fetch("http://127.0.0.1:8000/sessions");
        if (!res.ok) throw new Error("Failed to fetch sessions");
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

  return (
    <div className="max-w-4xl mx-auto mt-8 p-6 bg-white rounded shadow">
      <h2 className="text-2xl font-semibold mb-4">Recorded Sessions</h2>
      {loading && <p>Loading sessions...</p>}
      {error && <p className="text-red-600">{error}</p>}
      {!loading && !error && (
        <ul>
          {sessions.length === 0 && <p>No sessions found.</p>}
          {sessions.map((session) => (
            <li
              key={session.session_id}
              className="border-b py-2 flex justify-between items-center"
            >
              <div>
                <strong>{session.session_id}</strong> -{" "}
                {new Date(session.timestamp).toLocaleString()}
              </div>
              <a
                href={`http://127.0.0.1:8000/sessions/${session.session_id}`}
                target="_blank"
                rel="noreferrer"
                className="text-blue-600 hover:underline"
              >
                View Details
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
