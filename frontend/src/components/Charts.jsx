import React from 'react';

export default function Charts({ chartData }) {
  if (!chartData) return <div>Loading charts...</div>;

  return (
    <div className="charts-container">
      <h3>Performance Charts</h3>
      {/* Replace with chart components or libraries */}
      <pre>{JSON.stringify(chartData, null, 2)}</pre>
    </div>
  );
}
