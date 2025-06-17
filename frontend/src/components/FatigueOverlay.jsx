import React from "react";

const FatigueOverlay = ({ events }) => {
  if (!events || events.length === 0) {
    return null;
  }

  return (
    <div className="bg-yellow-100 border-l-4 border-yellow-500 p-4 my-4 rounded">
      <h3 className="font-bold text-yellow-800">Live Fatigue / Flaw Events:</h3>
      <ul className="list-disc list-inside text-sm mt-2">
        {events.map((e, i) => (
          <li key={i}>
            <span className="font-medium">{e.type}</span>: {e.value} @ {e.timestamp.toFixed(2)}s
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FatigueOverlay;
