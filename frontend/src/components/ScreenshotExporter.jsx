import React from 'react';
import html2canvas from 'html2canvas';

const ScreenshotExporter = () => {
  const exportScreenshot = () => {
    const input =
      document.getElementById('valuation-content') ||
      document.getElementById('report-content');
    if (!input) return;
    html2canvas(input, { scale: 2 }).then(canvas => {
      const link = document.createElement('a');
      link.download = 'formforge_screenshot.png';
      link.href = canvas.toDataURL('image/png');
      link.click();
    });
  };

  return (
    <button
      onClick={exportScreenshot}
      className="px-4 py-2 h-10 bg-[#008933] text-white rounded hover:bg-[#007f2a] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
    >
      Export Screenshot
    </button>
  );
};

export default ScreenshotExporter;
