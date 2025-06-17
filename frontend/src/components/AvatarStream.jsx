import React, { useEffect, useState } from 'react';

export default function AvatarStream() {
  const [avatarData, setAvatarData] = useState({});
  const [demoMode, setDemoMode] = useState(true);

  const staticData = {
    "athlete": "Athlete_1",
    "status": "active",
    "joints": {
      "joint_1": 28.9,
      "joint_2": 45.7,
      "joint_3": 14.2
    },
    "fatigue": 0.36,
    "timestamp": 1749500000
  };

  useEffect(() => {
    if (demoMode) {
      setAvatarData(staticData);
      return;
    }

    const fetchData = async () => {
      try {
        const res = await fetch('/avatar_state.json');
        const data = await res.json();
        setAvatarData(data);
      } catch (err) {
        console.error('Failed to load avatar_state.json:', err);
      }
    };

    const interval = setInterval(fetchData, 1000);
    return () => clearInterval(interval);
  }, [demoMode]);

  return (
    <div>
      <div className="flex justify-between items-center mb-2">
        <h2 className="text-xl font-semibold">🧠 Live Avatar Coaching</h2>
        <label className="text-sm text-gray-600">
          <input
            type="checkbox"
            checked={demoMode}
            onChange={() => setDemoMode(!demoMode)}
            className="mr-2"
          />
          Demo Mode
        </label>
      </div>
      <pre className="bg-gray-800 text-white p-4 rounded-xl text-xs overflow-x-auto">
        {JSON.stringify(avatarData, null, 2)}
      </pre>
    </div>
  );
}
