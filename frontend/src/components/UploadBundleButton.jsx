import React, { useState } from 'react';
import { uploadBundle } from '../api/upload.js';

const UploadBundleButton = () => {
  const [link, setLink] = useState('');

  const handleUpload = async () => {
    const resp = await fetch('/investor_bundle.zip');
    const blob = await resp.blob();
    const file = new File([blob], 'investor_bundle.zip');
    const result = await uploadBundle(file);
    setLink(result.url);
  };

  return (
    <div className="space-y-2">
      <button
        onClick={handleUpload}
        className="px-4 py-2 h-10 h-10 bg-purple-600 text-white rounded hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500"
      >
        Upload Bundle to S3
      </button>
      {link && (
        <a
          href={link}
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-600 underline focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
        >
          Download Bundle Link
        </a>
      )}
    </div>
  );
};

export default UploadBundleButton;
