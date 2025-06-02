import React from 'react';

export default function SessionTimeline({ keyMoments }) {
  return (
    <div className="mt-6">
      <h2 className="text-lg font-semibold">Key Timeline</h2>
      <ul className="space-y-2">
        {keyMoments.map((moment, i) => (
          <li key={i} className="border p-2 rounded bg-gray-100 hover:bg-gray-200">
            <strong>{moment.label}</strong> – {moment.timestamp}
          </li>
        ))}
      </ul>
    </div>
  );
}
