import React, { useEffect, useState } from 'react';

export default function RiskOverlay({ jointData }) {
  const [risk, setRisk] = useState(null);

  useEffect(() => {
    if (!jointData?.length) return;
    fetch('/api/biomech/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ joint_df: jointData }),
    })
      .then((res) => res.json())
      .then((data) => setRisk((data.risk_score * 100).toFixed(1)))
      .catch(() => setRisk('err'));
  }, [jointData]);

  return (
    <div className="absolute top-2 right-2 bg-white p-2 rounded shadow">
      <span className="font-bold">Risk:</span>{' '}
      {risk !== null ? `${risk}%` : '…'}
    </div>
  );
}
