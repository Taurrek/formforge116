import React from 'react';
import { downloadStrainCsv } from '../utils/downloadCsv';

const DownloadCsvButton = () => (
  <button
    onClick={downloadStrainCsv}
    className="bg-blue-500 text-white px-4 py-2 h-10 h-10 rounded hover:bg-blue-600"
  >
    Download Strain CSV
  </button>
);

export default DownloadCsvButton;
