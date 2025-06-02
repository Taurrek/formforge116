import React, { useState } from 'react';

export default function SportPredictor() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
    setError(null);
  };

  const handleSubmit = async () => {
    if (!file) {
      setError('Please select a CSV file first.');
      return;
    }
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch('http://localhost:8000/predict_sport_enhanced/', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.statusText}`);
      }

      const data = await response.json();

      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto p-6 bg-white rounded shadow mt-10">
      <h2 className="text-xl font-semibold mb-4">🏅 Predict Sport from Joint Data</h2>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button
        onClick={handleSubmit}
        className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"
        disabled={loading}
      >
        {loading ? 'Predicting...' : 'Predict Sport'}
      </button>

      {error && (
        <p className="mt-4 text-red-600 font-medium" role="alert">
          Error: {error}
        </p>
      )}

      {result && (
        <div className="mt-6 p-4 bg-gray-100 rounded">
          <p><strong>Predicted Sport:</strong> {result.predicted_sport}</p>
          <p><strong>Confidence:</strong> {(result.confidence * 100).toFixed(2)}%</p>
          <p><strong>Explanation:</strong> {result.explanation.join(', ')}</p>
        </div>
      )}
    </div>
  );
}
