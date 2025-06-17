import React, { useState, useEffect } from 'react';
import ProgressTracking from './ProgressTracking';

const Dashboard = () => {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    // Simulate progress incrementally over time
    const interval = setInterval(() => {
      setProgress((prev) => {
        if (prev < 100) return prev + 5; // Increase progress by 5% each interval
        clearInterval(interval); // Stop when progress reaches 100%
        return 100;
      });
    }, 500); // Update every 500ms

    return () => clearInterval(interval); // Clean up interval on unmount
  }, []);

  return (
    <div>
      <h1>Fatigue Detection Dashboard</h1>
      <ProgressTracking progress={progress} />
    </div>
  );
};

export default Dashboard;
