import React from "react";
import CameraStream from "./CameraStream";

export default function MultiAthleteDashboard({ athleteIds }) {
  const cols = athleteIds.length;
  const gridClass = "grid gap-4 grid-cols-" + cols;
  return (
    <div className={gridClass}>
      {athleteIds.map((id) => (
        <div key={id} className="p-2 border rounded-lg shadow-sm">
          <h3 className="font-semibold mb-2">Camera: {id}</h3>
          <CameraStream athleteId={id} />
        </div>
      ))}
    </div>
  );
}
