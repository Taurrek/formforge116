import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Reports() {
  const [records, setRecords] = useState([]);
  useEffect(() => {
    axios.get('/api/admin/performance')
      .then(res => setRecords(res.data))
      .catch(console.error);
  }, []);
  return (
    <div style={{ padding: 20 }}>
      <h2>Performance Records</h2>
      <table border="1" cellPadding="8">
        <thead><tr><th>Timestamp</th><th>Value</th><th>Athlete ID</th></tr></thead>
        <tbody>
          {records.map((r,i) => (
            <tr key={i}>
              <td>{new Date(r.timestamp * 1000).toLocaleString()}</td>
              <td>{r.value}</td>
              <td>{r.athlete_id}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
