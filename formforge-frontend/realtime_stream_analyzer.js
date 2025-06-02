// src/components/realtime_stream_analyzer.jsx
import React, { useEffect, useState, useRef } from "react";

export default function RealTimeStreamAnalyzer({ streamUrl }) {
  const [poseQuality, setPoseQuality] = useState("Good");
  const [warnings, setWarnings] = useState([]);
  const videoRef = useRef(null);

  useEffect(() => {
    let ws;
    let frameCount = 0;

    function connect() {
      ws = new WebSocket(streamUrl);

      ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        setPoseQuality(data.quality);
        setWarnings(data.warnings || []);
        frameCount++;
      };

      ws.onerror = () => {
        setPoseQuality("Error: Connection lost");
        setWarnings([]);
      };

      ws.onclose = () => {
        setPoseQuality("Disconnected");
      };
    }

    connect();

    return () => {
      if (ws) ws.close();
    };
  }, [streamUrl]);

  return (
    <div className="p-4 border rounded shadow-md bg-white">
      <video
        ref={videoRef}
        className="w-full rounded"
        autoPlay
        muted
        controls
      />
      <div className="mt-3 text-center">
        <h3
          className={`text-xl font-bold ${
            poseQuality === "Good" ? "text-green-600" : "text-red-600"
          }`}
        >
          Pose Quality: {poseQuality}
        </h3>
        {warnings.length > 0 && (
          <ul className="mt-2 text-left text-red-500">
            {warnings.map((warn, i) => (
              <li key={i}>⚠️ {warn}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
