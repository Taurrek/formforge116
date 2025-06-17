import React, { useState, useEffect } from "react";

const SessionDashboard = () => {
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    fetch("/api/sessions")
      .then((res) => res.json())
      .then((data) => setSessions(data.sessions || []));
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">📊 Session Dashboard</h2>
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
