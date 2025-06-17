import React from 'react';

const ReportSummary = ({ data }) => {
  const totalAthletes = data.athleteCount;
  const avgFatigue = data.avgFatigue?.toFixed(2);
  const peakFatigue = data.peakFatigue?.value.toFixed(2);
  const peakTime = data.peakFatigue
    ? new Date(data.peakFatigue.timestamp * 1000).toLocaleTimeString()
    : '';
  return (
    <div id="report-content" className="p-4 bg-white">
      <h1 className="text-2xl font-bold mb-4">FormForge Session Summary</h1>
      <p className="mb-2"><strong>Total Athletes:</strong> {totalAthletes}</p>
      <p className="mb-2"><strong>Average Fatigue Level:</strong> {avgFatigue}</p>
      <p className="mb-2"><strong>Peak Fatigue:</strong> {peakFatigue} at {peakTime}</p>
      <h2 className="text-xl font-semibold mt-4 mb-2">Coaching Feedback Highlights</h2>
      <ul className="list-disc list-inside">
        {data.feedbackHighlights.map((item, idx) => (
          <li key={idx}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default ReportSummary;
