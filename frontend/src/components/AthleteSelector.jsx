import React from "react";

const AthleteSelector = ({ athletes, selected, onChange }) => {
  return (
    <div className="p-2">
      <label className="mr-2 font-bold">Select Athlete:</label>
      <select
        className="border rounded p-1"
        value={selected}
        onChange={(e) => onChange(e.target.value)}
      >
        {athletes.map((id) => (
          <option key={id} value={id}>
            {id}
          </option>
        ))}
      </select>
    </div>
  );
};

export default AthleteSelector;
