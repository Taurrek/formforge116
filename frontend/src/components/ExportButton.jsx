import React from 'react';

const ExportButton = ({ data }) => {
  const exportToCSV = () => {
    const csvData = data.map(row => `${row.timestamp},${row.fatigueLevel}`);
    const csvContent = "data:text/csv;charset=utf-8," + csvData.join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "session_report.csv");
    link.click();
  };

  return <button onClick={exportToCSV}>Export to CSV</button>;
};

export default ExportButton;
