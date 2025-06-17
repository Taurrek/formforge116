import React, { useState, useEffect } from "react";

export default function CameraStream({ athleteId }) {
  const [frames, setFrames] = useState([]);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8005/ws/cam/" + athleteId);
    ws.onmessage = (evt) => {
      setFrames((prev) => [...prev.slice(-9), JSON.parse(evt.data)]);
    };
    return () => ws.close();
  }, [athleteId]);

  return (
    <div className="text-xs">
      {frames.map((f, i) => (
        <div key={i}>
          {new Date(f.timestamp * 1000).toLocaleTimeString()}:  
          pose={f.pose_score.toFixed(2)}, fatigue={f.fatigue.toFixed(2)}
        </div>
      ))}
    </div>
  );
}
