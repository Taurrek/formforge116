import React, { useState } from 'react';

export default function UploadGoldenModel() {
  const [payload, setPayload] = useState('');
  const [message, setMessage] = useState('');

  const handleUpload = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/golden-model/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payload,
      });
      const text = await response.text();
      if (response.ok) {
        setMessage('Success: ' + text);
      } else {
        setMessage('Upload failed (' + response.status + '): ' + text);
      }
    } catch (error) {
      setMessage('Error: ' + error.message);
    }
  };

  return (
    <div>
      <h3>Upload Golden Model</h3>
      <textarea
        value={payload}
        onChange={e => setPayload(e.target.value)}
        placeholder='{"sport":"running",...}'
        rows={8}
        cols={60}
      />
      <br />
      <button onClick={handleUpload}>Upload</button>
      <pre style={{ whiteSpace: 'pre-wrap', marginTop: 8 }}>
        {message}
      </pre>
    </div>
  );
}
