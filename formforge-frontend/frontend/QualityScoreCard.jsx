// src/components/QualityScoreCard.jsx
import React from 'react';

const QualityScoreCard = ({ score }) => {
  let qualityLabel = 'Unknown';
  let color = 'bg-gray-300';

  if (score >= 85) {
    qualityLabel = 'Elite';
    color = 'bg-green-500';
  } else if (score >= 70) {
    qualityLabel = 'Pro-Level';
    color = 'bg-blue-500';
  } else if (score >= 50) {
    qualityLabel = 'Intermediate';
    color = 'bg-yellow-400';
  } else {
    qualityLabel = 'Needs Improvement';
    color = 'bg-red-500';
  }

  return (
    <div className={`p-4 text-white ${color} rounded shadow`}>
      <h3 className="text-lg font-semibold">{qualityLabel}</h3>
      <p className="text-xl">{score}/100</p>
    </div>
  );
};

export default QualityScoreCard;
