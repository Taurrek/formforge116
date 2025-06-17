import React from "react";

export default function Chart({ title, data }) {
  return (
    <div className="border p-2 rounded">
      <h4 className="text-sm font-medium mb-1">{title}</h4>
      <ul className="text-xs">
        {data.slice(-10).map((pt, i) => (
          <li key={i}>
            {new Date(pt.x * 1000).toLocaleTimeString()}: {pt.y.toFixed(2)}
          </li>
        ))}
      </ul>
    </div>
  );
}
