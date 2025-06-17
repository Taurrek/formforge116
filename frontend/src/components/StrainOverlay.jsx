import React from "react";

function colorClass(strain) {
  if (strain > 0.8) return "bg-red-500";
  if (strain > 0.5) return "bg-yellow-500";
  return "bg-green-500";
}

export default function StrainOverlay({ joints }) {
  return (
    <div className="relative">
      {joints.map((j, i) => (
        <div
          key={i}
          className={colorClass(j.strain) + " rounded-full w-4 h-4 absolute"}
          style={{ left: j.x - 2, top: j.y - 2 }}
          title={j.name + ": " + j.strain.toFixed(2)}
        />
      ))}
    </div>
  );
}
