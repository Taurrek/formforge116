import React, { useState, useEffect } from "react";
import Chart from "./Chart";

export default function SensorFusionDashboard({ athleteId }) {
  const [data, setData] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8003/ws/fused-metrics?athleteId=" + athleteId);

    ws.onmessage = (evt) => {
      const pt = JSON.parse(evt.data);
      setData((prev) => [...prev, pt]);

      // UI alerts on the exact demo crossings: hr > 82, vel > 0.75
      if (pt.hr > 82) {
        setAlerts((a) => [...a, "High HR: " + pt.hr]);
      }
      if (pt.joint_vel > 0.75) {
        setAlerts((a) => [...a, "High Velocity: " + pt.joint_vel.toFixed(2)]);
      }
    };

    ws.onclose = () => console.log("WebSocket closed");
    return () => ws.close();
  }, [athleteId]);

  return (
    <div>
      {alerts.length > 0 && (
        <div className="mb-4 p-2 bg-red-100 border border-red-400 text-red-700 rounded">
          {alerts.map((msg, i) => (
            <div key={i}>{msg}</div>
          ))}
        </div>
      )}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Chart title="Joint Velocity" data={data.map((d) => ({ x: d.timestamp, y: d.joint_vel }))}/>
        <Chart title="Heart Rate"       data={data.map((d) => ({ x: d.timestamp, y: d.hr }))}/>
      </div>
    </div>
  );
}
