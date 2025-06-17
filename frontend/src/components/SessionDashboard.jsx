import React, { useEffect, useState } from "react";

const SessionDashboard = () => {
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8001/api/sessions")
      .then((res) => res.json())
      .then((data) => setSessions(data.sessions || []));
  }, []);

  return (
    <div>
      {sessions.map((s, i) => (
        <div key={i} className="mb-2 p-2 border rounded shadow">
          <p><strong>Athlete:</strong> {s.athlete}</p>
          <p><strong>Sport:</strong> {s.sport}</p>
          <p><strong>Date:</strong> {new Date(s.date).toLocaleDateString()}</p>
          <p><strong>Score:</strong> {s.score}</p>
        </div>
      ))}
    </div>
  );
};

export default SessionDashboard;
