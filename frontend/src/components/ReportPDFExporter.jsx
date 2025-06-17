import React from 'react';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

const ReportPDFExporter = () => {
  const exportPDF = () => {
    const input = document.getElementById('report-content');
    if (!input) return;
    html2canvas(input, { scale: 2 }).then(canvas => {
      const imgData = canvas.toDataURL('image/png');
      const pdf = new jsPDF('p', 'pt', 'a4');
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = (canvas.height * pdfWidth) / canvas.width;
      pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
      pdf.save('formforge_report.pdf');
    });
  };

  return (
    <button
      onClick={exportPDF}
      className="px-4 py-2 h-10 h-10 bg-blue-600 text-white rounded hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
    >
      Export Report to PDF
    </button>
  );
};

export default ReportPDFExporter;
