// src/components/AthleteProgressChart.jsx
import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';

const AthleteProgressChart = ({ athleteId }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(`/api/athlete/${athleteId}/progress`)
      .then(res => res.json())
      .then(setData)
      .catch(console.error);
  }, [athleteId]);

  const chartData = {
    labels: data.map((d) => d.date),
    datasets: [
      {
        label: 'Motion Score',
        data: data.map((d) => d.motionScore),
        borderColor: '#3b82f6',
        backgroundColor: 'rgba(59,130,246,0.2)',
        tension: 0.3,
      },
    ],
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-semibold mb-4">Progress Tracker</h2>
      <Line data={chartData} />
    </div>
  );
};

export default AthleteProgressChart;
