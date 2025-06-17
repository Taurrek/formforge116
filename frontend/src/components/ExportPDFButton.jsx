import React from 'react';
import { jsPDF } from "jspdf";

const ExportPDFButton = ({ data }) => {
  const exportToPDF = () => {
    const doc = new jsPDF();
    doc.text("Session Report", 10, 10);
    data.forEach((row, index) => {
      doc.text(`${row.timestamp}: ${row.fatigueLevel}`, 10, 20 + (index * 10));
    });
    doc.save("session_report.pdf");
  };

  return <button onClick={exportToPDF}>Export to PDF</button>;
};

export default ExportPDFButton;
