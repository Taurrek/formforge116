// src/components/PerformanceRadar.jsx
import React, { useEffect, useState } from 'react';
import { Radar } from 'react-chartjs-2';
import 'chart.js/auto';

const PerformanceRadar = ({ sessionId }) => {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    fetch(`/api/session/${sessionId}/metrics`)
      .then(res => res.json())
      .then(data => setMetrics(data))
      .catch(err => console.error('Failed to load metrics', err));
  }, [sessionId]);

  if (!metrics) return <div className="text-center mt-10">Loading radar chart...</div>;

  const chartData = {
    labels: ['Speed', 'Balance', 'Symmetry', 'Stability', 'Control', 'Endurance'],
    datasets: [
      {
        label: 'Performance Metrics',
        data: [
          metrics.speedScore,
          metrics.balanceScore,
          metrics.symmetryScore,
          metrics.stabilityScore,
          metrics.controlScore,
          metrics.enduranceScore,
        ],
        backgroundColor: 'rgba(34, 197, 94, 0.4)',
        borderColor: '#22c55e',
        borderWidth: 2,
      },
    ],
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-semibold mb-4 text-center">Performance Overview</h2>
      <Radar data={chartData} />
    </div>
  );
};

export default PerformanceRadar;
