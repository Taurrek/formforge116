import React, { useState } from 'react';
import axios from 'axios';

export default function Highlights({ session }) {
  const [indices, setIndices] = useState([]);
  const fetch = () => {
    axios.post('/highlights', { session_id: session.id, frames: session.frames })
      .then(r => setIndices(r.data.highlights))
      .catch(console.error);
  };
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Highlights</h1>
      <button onClick={fetch} className="px-4 py-2 h-10 h-10 bg-blue-500 text-white rounded">
        Fetch Top Highlights
      </button>
      <ul className="mt-2">
        {indices.map(i => <li key={i}>Frame #{i}</li>)}
      </ul>
    </div>
  );
}
