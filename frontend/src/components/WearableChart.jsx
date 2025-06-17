import React from "react";
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from "recharts";

const WearableChart = ({ readings }) => {
  if (!readings || readings.length === 0) {
    return <p className="text-gray-500 italic">No wearable data available.</p>;
  }

  return (
    <div className="w-full h-64 bg-white rounded-xl shadow p-4">
      <h2 className="text-lg font-bold mb-2">Wearable Sensor Data</h2>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={readings}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="timestamp" label={{ value: "Time (s)", position: "insideBottom", offset: -5 }} />
          <YAxis yAxisId="left" label={{ value: "Heart Rate", angle: -90, position: "insideLeft" }} />
          <YAxis yAxisId="right" orientation="right" label={{ value: "Accel", angle: -90, position: "insideRight" }} />
          <Tooltip />
          <Legend />
          <Line yAxisId="left" type="monotone" dataKey="heart_rate" stroke="#8884d8" name="Heart Rate" />
          <Line yAxisId="right" type="monotone" dataKey="accel" stroke="#82ca9d" name="Accel" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default WearableChart;
