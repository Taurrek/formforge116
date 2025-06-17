import React, { useState, useEffect } from 'react';
import ReportSummary from './ReportSummary.jsx';
import ReportPDFExporter from './ReportPDFExporter.jsx';
import ScreenshotExporter from './ScreenshotExporter.jsx';
import ValuationBrief from './ValuationBrief.jsx';
import UploadBundleButton from './UploadBundleButton.jsx';
import { fetchReportData } from '../api/report.js';
import { fetchValuationData } from '../api/valuation.js';

const GoldenShowcase = () => {
  const [reportData, setReportData] = useState(null);
  const [valuationData, setValuationData] = useState(null);

  useEffect(() => {
    fetchReportData().then(setReportData);
    fetchValuationData().then(setValuationData);
  }, []);

  if (!reportData || !valuationData) return <div>Loading...</div>;

  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <ReportSummary data={reportData} />
      <div className="flex justify-center space-x-4">
        <ReportPDFExporter />
        <ScreenshotExporter />
        <UploadBundleButton />
      </div>
      <ValuationBrief data={valuationData} />
    </div>
  );
};

export default GoldenShowcase;
