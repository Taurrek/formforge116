// src/pages/TrainerDashboard.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TrainerDashboard = () => {
  const [sessions, setSessions] = useState([]);
  const [selectedSession, setSelectedSession] = useState(null);
  const [notes, setNotes] = useState('');
  const [feedback, setFeedback] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/sessions')
      .then(res => setSessions(res.data.sessions))
      .catch(() => setFeedback('Failed to load sessions.'));
  }, []);

  const handleSaveNotes = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/trainer_notes', {
        session_id: selectedSession,
        notes,
      });
      setFeedback('Notes saved!');
    } catch {
      setFeedback('Failed to save notes.');
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Trainer Dashboard</h2>
      <select
        className="border p-2"
        onChange={(e) => setSelectedSession(e.target.value)}
      >
        <option value="">Select Session</option>
        {sessions.map((s) => (
          <option key={s} value={s}>{s}</option>
        ))}
      </select>
      <textarea
        className="w-full h-32 border mt-4 p-2"
        placeholder="Enter motion notes..."
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
      />
      <button onClick={handleSaveNotes} className="bg-green-500 text-white px-4 py-2 mt-2 rounded">
        Save Notes
      </button>
      <p className="mt-2">{feedback}</p>
    </div>
  );
};

export default TrainerDashboard;
