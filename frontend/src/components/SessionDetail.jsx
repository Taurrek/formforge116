import React, { useEffect, useState } from 'react';

function SessionDetail({ sessionId }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5001/api/session/${sessionId}`)
      .then(res => res.json())
      .then(setData)
      .catch(err => console.error('Failed to load session data', err));
  }, [sessionId]);

  if (!data) return <p>Loading session data...</p>;

  return (
    <div>
      <h2>Session ID: {sessionId}</h2>
      <pre style={{ background: '#f0f0f0', padding: '1rem' }}>
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}

export default SessionDetail;
