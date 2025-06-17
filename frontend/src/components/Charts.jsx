import React from "react";

const Charts = ({ events }) => {
  if (!events || events.length === 0) {
    return <p className="text-gray-500 italic">No chart data available.</p>;
  }

  return (
    <div className="bg-white rounded-xl shadow p-4">
      <h2 className="text-lg font-bold mb-2">Fatigue + Flaw Events</h2>
      <ul className="space-y-1 text-sm">
        {events.map((e, i) => (
          <li key={i} className="flex justify-between border-b py-1">
            <span className="text-gray-600">{e.type.toUpperCase()}</span>
            <span className="text-gray-800">{e.value}</span>
            <span className="text-gray-500">{e.timestamp.toFixed(2)}s</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Charts;
