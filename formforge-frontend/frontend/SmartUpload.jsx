// src/pages/SmartUpload.jsx
import React, { useState } from 'react';
import axios from 'axios';

const SmartUpload = () => {
  const [file, setFile] = useState(null);
  const [feedback, setFeedback] = useState('');
  const [motionType, setMotionType] = useState('Unknown');
  const [uploadScore, setUploadScore] = useState(null);

  const detectMotionType = (filename) => {
    if (filename.toLowerCase().includes('jump')) return 'Jumping';
    if (filename.toLowerCase().includes('run')) return 'Running';
    if (filename.toLowerCase().includes('throw')) return 'Throwing';
    return 'Unknown';
  };

  const handleChange = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    setMotionType(detectMotionType(selected.name));
    setFeedback('Ready to upload.');
  };

  const handleUpload = async () => {
    if (!file) {
      setFeedback('Please select a video first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      setFeedback('Uploading...');
      const res = await axios.post('http://127.0.0.1:8000/upload', formData);
      setUploadScore(Math.floor(Math.random() * 100)); // Simulated smart score
      setFeedback('Upload complete!');
    } catch (error) {
      setFeedback('Upload failed.');
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold">Smart Video Upload</h2>
      <input type="file" onChange={handleChange} accept="video/*" />
      <p className="mt-2 text-sm">Detected Motion: <strong>{motionType}</strong></p>
      <button onClick={handleUpload} className="mt-4 bg-blue-500 text-white px-4 py-2 rounded">
        Upload
      </button>
      <p className="mt-4">{feedback}</p>
      {uploadScore !== null && <p>Upload Quality Score: {uploadScore}/100</p>}
    </div>
  );
};

export default SmartUpload;
