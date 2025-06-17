import React, { useState } from 'react';

export default function GoldenDiff() {
  const [payload, setPayload] = useState('');
  const [message, setMessage] = useState('');

  const handleCompare = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/compare-frame/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payload,
      });
      const text = await response.text();
      if (response.ok) {
        setMessage(text);
      } else {
        setMessage('Compare failed (' + response.status + '): ' + text);
      }
    } catch (error) {
      setMessage('Error: ' + error.message);
    }
  };

  return (
    <div>
      <h3>Golden Model Comparison</h3>
      <textarea
        value={payload}
        onChange={e => setPayload(e.target.value)}
        placeholder='Paste comparison JSON here'
        rows={8}
        cols={60}
      />
      <br />
      <button onClick={handleCompare}>Compare</button>
      <pre style={{ whiteSpace: 'pre-wrap', marginTop: 8 }}>
        {message}
      </pre>
    </div>
  );
}
