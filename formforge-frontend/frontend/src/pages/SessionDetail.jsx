// src/pages/SessionDetail.jsx
import React, { useEffect, useState } from 'react';
import { getFeedback, getChart } from '../api/api';

function SessionDetail({ sessionId = 'session1' }) {
  const [feedback, setFeedback] = useState(null);
  const [chartData, setChartData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      try {
        const feedbackRes = await getFeedback(sessionId);
        const chartRes = await getChart(sessionId);
        setFeedback(feedbackRes);
        setChartData(chartRes);
        setError(null);
      } catch (err) {
        console.error(err);
        setError('Failed to load session data. Make sure the backend is running.');
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, [sessionId]);

  if (loading) return <div>Loading session data...</div>;
  if (error) return <div style={{ color: 'red' }}>Error: {error}</div>;

  return (
    <div style={{ padding: '1rem' }}>
      <h2>Session Detail: {sessionId}</h2>

      <section>
        <h3>📋 AI Feedback</h3>
        <pre style={{ background: '#f0f0f0', padding: '1rem' }}>
          {JSON.stringify(feedback, null, 2)}
        </pre>
      </section>

      <section>
        <h3>📈 Chart Data</h3>
        <pre style={{ background: '#f0f0f0', padding: '1rem' }}>
          {JSON.stringify(chartData, null, 2)}
        </pre>
      </section>

      <section>
        <h3>🧠 Insights</h3>
        <ul>
          <li>Highlight major flaws or tips from feedback here later</li>
          <li>Render radar charts or graphs using chartData soon</li>
        </ul>
      </section>
    </div>
  );
}

export default SessionDetail;
