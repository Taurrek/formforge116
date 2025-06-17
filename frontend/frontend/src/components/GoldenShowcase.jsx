import React, { useEffect, useState } from 'react';
import AvatarStream from './AvatarStream';
import SessionDashboard from './SessionDashboard';
import AutoCoach from './AutoCoach';

export default function GoldenShowcase() {
  const [fatigueEvents] = useState([
    { time: 2, event: 'Fatigue spike', level: 0.8 },
    { time: 5, event: 'Knee instability', level: 0.7 },
    { time: 9, event: 'Low posture control', level: 0.6 },
  ]);
  const [timestamp, setTimestamp] = useState(0);

  useEffect(() => {
    let current = 0;
    const interval = setInterval(() => {
      current += 1;
      setTimestamp(current);
      if (current > 12) current = 0;
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const handleExport = () => {
    try {
      const report = {
        athlete: 'Athlete_1',
        timestamp: Date.now(),
        fatigue_timeline: fatigueEvents,
        coaching_feedback: [
          "Maintain upright torso during sprint.",
          "Pump arms straight front-to-back.",
          "Lift knees higher to increase stride efficiency."
        ]
      };

      const jsonString = JSON.stringify(report, null, 2);
      const blob = new Blob([jsonString], { type: 'application/json' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'formforge_report.json';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
    } catch (err) {
      alert("Export failed: " + err.message);
      console.error(err);
    }
  };

  return (
    <div className="p-4 space-y-4">
      <div className="text-2xl font-bold">🏅 FormForge Demo Showcase</div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="rounded-xl shadow p-2 border">
          <AvatarStream />
        </div>
        <div className="rounded-xl shadow p-2 border">
          <SessionDashboard />
        </div>
      </div>

      <div className="bg-gray-100 p-4 rounded-xl shadow">
        <div className="text-xl font-semibold mb-2">⚠️ Fatigue Timeline</div>
        <ul className="list-disc pl-6 text-sm">
          {fatigueEvents.map((e, idx) => (
            <li key={idx} className={timestamp >= e.time ? "text-red-600 font-bold" : "text-gray-600"}>
              ⏱️ {e.time}s — {e.event} (fatigue={e.level})
            </li>
          ))}
        </ul>
        <div className="mt-2 text-xs text-gray-500">⏳ Timestamp: {timestamp}s</div>
      </div>

      <div className="rounded-xl shadow p-2 border">
        <AutoCoach />
      </div>

      <div className="flex gap-4 mt-4">
        <button
          onClick={handleExport}
          className="bg-blue-600 text-white px-4 py-2 rounded-xl shadow">
          🧾 Export Report
        </button>
        <button className="bg-green-600 text-white px-4 py-2 rounded-xl shadow">
          🔁 Replay
        </button>
        <button className="bg-purple-600 text-white px-4 py-2 rounded-xl shadow">
          📊 Compare Against Golden
        </button>
      </div>
    </div>
  );
}
