// src/pages/AnalysisViewer.jsx
import React, { useState } from 'react';

const AnalysisViewer = ({ videoUrl, overlayData }) => {
  const [showAngles, setShowAngles] = useState(true);
  const [showVectors, setShowVectors] = useState(true);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Motion Analysis</h2>
      <video src={videoUrl} controls width="100%" className="mb-4" />
      <div className="flex gap-4">
        <label>
          <input type="checkbox" checked={showAngles} onChange={() => setShowAngles(!showAngles)} />
          Joint Angles
        </label>
        <label>
          <input type="checkbox" checked={showVectors} onChange={() => setShowVectors(!showVectors)} />
          Velocity Vectors
        </label>
      </div>
      <div className="mt-4">
        {showAngles && <p>🧠 Showing joint angles...</p>}
        {showVectors && <p>🏃 Showing motion vectors...</p>}
      </div>
    </div>
  );
};

export default AnalysisViewer;
