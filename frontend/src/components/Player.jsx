import React from 'react';

export default function Player({ sessionData }) {
  if (!sessionData) return <div>Loading player data...</div>;

  return (
    <div className="player-card">
      <h2>{sessionData.playerName || 'Player Name'}</h2>
      <p>Session Date: {sessionData.sessionDate || 'N/A'}</p>
      {/* Add more player details here */}
    </div>
  );
}
