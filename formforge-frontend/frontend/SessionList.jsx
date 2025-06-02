// src/components/SessionList.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const SessionList = ({ onSelect }) => {
  const [sessions, setSessions] = useState([]);
  const [query, setQuery] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/sessions')
      .then((res) => setSessions(res.data.sessions))
      .catch(() => setSessions([]));
  }, []);

  const filtered = sessions.filter((s) => s.toLowerCase().includes(query.toLowerCase()));

  return (
    <div className="p-4">
      <input
        type="text"
        placeholder="Search sessions..."
        className="border p-2 mb-2 w-full"
        onChange={(e) => setQuery(e.target.value)}
      />
      <ul className="list-disc pl-4">
        {filtered.map((s, i) => (
          <li key={i} onClick={() => onSelect(s)} className="cursor-pointer hover:underline">
            {s}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SessionList;
