import React from 'react';

const ExportButtons = ({ fatigueEvents }) => {
  const exportCSV = () => {
    const header = "timestamp,athlete_id,event_type,value\n";
    const rows = fatigueEvents.map(e => `${e.timestamp},${e.athlete_id},${e.event_type},${e.value}`).join("\n");
    const blob = new Blob([header + rows], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'fatigue_events.csv';
    link.click();
  };

  const exportPDF = async () => {
    const { jsPDF } = await import('jspdf');
    const doc = new jsPDF();
    doc.setFontSize(14);
    doc.text("Fatigue Events Report", 20, 20);
    fatigueEvents.forEach((e, i) => {
      doc.text(`${e.timestamp} | ${e.athlete_id} | ${e.event_type} | ${e.value}`, 20, 30 + i * 10);
    });
    doc.save('fatigue_events.pdf');
  };

  return (
    <div className="my-4 space-x-4">
      <button onClick={exportCSV} className="bg-blue-600 text-white px-4 py-2 h-10 h-10 rounded">Export CSV</button>
      <button onClick={exportPDF} className="bg-green-600 text-white px-4 py-2 h-10 h-10 rounded">Export PDF</button>
    </div>
  );
};

export default ExportButtons;
