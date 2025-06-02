import React, { useState } from 'react';

export default function NoteAI() {
  const [note, setNote] = useState('');
  const [generated, setGenerated] = useState(null);

  const generateInsight = () => {
    if (!note) return;
    // Simulated AI insight
    setGenerated(`Coach Insight: Based on your note – "${note}", athlete should focus on stability during takeoff.`);
  };

  return (
    <div className="mt-6">
      <h2 className="text-lg font-semibold">NoteAI Assistant</h2>
      <textarea
        className="w-full p-2 border rounded"
        rows={4}
        placeholder="Write your observation here..."
        value={note}
        onChange={(e) => setNote(e.target.value)}
      />
      <button onClick={generateInsight} className="mt-2 bg-blue-600 text-white px-4 py-1 rounded">
        Generate AI Insight
      </button>
      {generated && <div className="mt-2 text-green-700">{generated}</div>}
    </div>
  );
}
