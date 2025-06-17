import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";

const ChartOverlay = ({ fatigueEvents }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const ctx = canvasRef.current.getContext("2d");

    const data = {
      labels: fatigueEvents.map(e => e.timestamp),
      datasets: [{
        label: "Fatigue Level",
        data: fatigueEvents.map(e => e.fatigue),
        borderColor: "red",
        fill: false,
        tension: 0.4,
      }],
    };

    const options = {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: "Fatigue Trendline",
        },
      },
      scales: {
        y: {
          beginAtZero: true,
          min: 0,
          max: 1,
        },
      },
    };

    const chart = new Chart(ctx, {
      type: "line",
      data,
      options,
    });

    return () => chart.destroy();
  }, [fatigueEvents]);

  return (
    <div style={{ width: "100%", marginTop: "2rem" }}>
      <canvas ref={canvasRef} />
    </div>
  );
};

export default ChartOverlay;
