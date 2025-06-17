import React from "react";

export default function StrainLoader() {
  const downloadCsv = async () => {
    try {
      // Note: since Vite serves everything in /public at “/”, we fetch from "/output/sim_output.json"
      const res = await fetch("/output/sim_output.json");
      if (!res.ok) throw new Error("Failed to fetch sim_output.json");
      const json = await res.json();

      // Build CSV rows
      const rows = [["timestamp","joint","strain"]];
      json.strain_timeline.forEach(entry => {
        const t = entry.timestamp;
        Object.entries(entry.strained_joints).forEach(([joint, strain]) => {
          rows.push([t, joint, strain]);
        });
      });

      // Join into a single string
      const csvContent = rows.map(r => r.join(",")).join("\n");
      const blob = new Blob([csvContent], { type: "text/csv" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "strain_timeline.csv";
      a.click();
      URL.revokeObjectURL(url);
    } catch (err) {
      alert(err.message);
    }
  };

  return (
    <div className="mt-4">
      <button
        onClick={downloadCsv}
        className="px-4 py-2 h-10 h-10 bg-blue-600 text-white rounded"
      >
        Download CSV
      </button>
    </div>
  );
}
