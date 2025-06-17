import React, { useEffect, useState } from "react";

const LiveFeed = () => {
  const [events, setEvents] = useState([]);
  const [athletes, setAthletes] = useState([]);
  const [selectedAthlete, setSelectedAthlete] = useState("All");

  useEffect(() => {
    fetch("/streamed_fatigue_feed.json")
      .then((res) => res.json())
      .then((data) => {
        setEvents(data);
        const uniq = Array.from(
          new Set(data.map((e) => e.athlete).filter((a) => !!a))
        );
        setAthletes(uniq);
      })
      .catch((err) => console.error(err));
  }, []);

  const filtered =
    selectedAthlete === "All"
      ? events
      : events.filter((e) => e.athlete === selectedAthlete);

  return (
    <div className="bg-white p-4 rounded-lg shadow">
      <h2 className="text-xl font-semibold mb-2">📡 Live Streamed Fatigue Feed</h2>
      <div className="mb-4">
        <label className="mr-2 font-medium">Filter by Athlete:</label>
        <select
          value={selectedAthlete}
          onChange={(e) => setSelectedAthlete(e.target.value)}
          className="border border-gray-300 rounded px-2 py-1"
        >
          <option value="All">All</option>
          {athletes.map((ath) => (
            <option key={ath} value={ath}>
              {ath}
            </option>
          ))}
        </select>
      </div>
      <ul className="space-y-2">
        {filtered.map((e, i) => (
          <li key={i} className="border border-gray-200 p-2 rounded">
            <div className="font-bold">
              {e.athlete
                ? e.athlete + " @ " + e.timestamp.toFixed(2) + "s"
                : e.timestamp.toFixed(2) + "s"}
            </div>
            {e.fatigue && e.fatigue.length > 0 && (
              <div className="text-yellow-700">
                Fatigue: {e.fatigue.join(", ")}
              </div>
            )}
            {e.flaws && e.flaws.length > 0 && (
              <div className="text-red-600">
                Flaws: {e.flaws.join(", ")}
              </div>
            )}
            {e.wearables && (
              <div className="text-gray-600">
                HR: {e.wearables.heart_rate || "–"}, Accel: {e.wearables.accel || "–"}
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LiveFeed;
