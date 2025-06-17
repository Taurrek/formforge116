import React, { useEffect, useState } from 'react';

export default function AutoCoach() {
  const [feedback, setFeedback] = useState(null);

  useEffect(() => {
    // Try to load local feedback JSON, fallback to static
    fetch('/auto_feedback.json')
      .then((res) => res.json())
      .then((data) => setFeedback(data))
      .catch(() =>
        setFeedback({
          comments: [
            'Maintain upright torso during sprint.',
            'Pump arms straight front-to-back.',
            'Lift knees higher to increase stride efficiency.',
          ],
        })
      );
  }, []);

  return (
    <div>
      <h2 className="text-xl font-semibold mb-2">🎯 Auto-Coach Recommendations</h2>
      <ul className="list-disc pl-6 text-sm text-gray-800">
        {(feedback?.comments || []).map((c, idx) => (
          <li key={idx}>{c}</li>
        ))}
      </ul>
    </div>
  );
}
