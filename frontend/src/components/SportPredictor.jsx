import React, { useState } from "react";

export default function SportPredictor() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
    setError(null);
  };

  const handlePredict = async () => {
    if (!file) {
      setError("Please select a CSV file first.");
      return;
    }
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const formData = new FormData();
      formData.append("file", file);
      const response = await fetch(
        "http://localhost:8000/predict_sport_enhanced/",
        { method: "POST", body: formData }
      );
      if (!response.ok) throw new Error("Prediction request failed.");
      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message || "Unknown error");
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setFile(null);
    setResult(null);
    setError(null);
  };

  return (
    <div className="max-w-lg mx-auto mt-10 p-6 border rounded shadow-md bg-white">
      <h1 className="text-2xl font-bold mb-6 text-center">🏅 Predict Sport from Joint Data</h1>

      <input
        type="file"
        accept=".csv"
        onChange={handleFileChange}
        className="block w-full mb-6 border rounded px-3 py-2"
      />

      <div className="flex gap-4 mb-6">
        <button
          onClick={handlePredict}
          disabled={loading || !file}
          className={`flex-1 py-2 rounded text-white ${
            loading || !file ? "bg-gray-400 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-700"
          }`}
        >
          {loading ? "Predicting..." : "Predict Sport"}
        </button>
        <button
          onClick={handleClear}
          disabled={loading && !file}
          className="flex-1 py-2 rounded bg-gray-300 hover:bg-gray-400"
        >
          Clear
        </button>
      </div>

      {error && <div className="mb-6 text-red-600 font-semibold">{error}</div>}

      {result && (
        <div>
          <h2 className="text-xl font-semibold mb-4">Prediction Result</h2>
          <p className="mb-2">
            <strong>Predicted Sport:</strong> {result.predicted_sport}
          </p>
          <p className="mb-2">
            <strong>Confidence:</strong> {(result.confidence * 100).toFixed(1)}%
          </p>

          <div className="w-full bg-gray-200 rounded h-5 mb-4">
            <div
              className="bg-green-600 h-5 rounded"
              style={{ width: `${(result.confidence * 100).toFixed(1)}%` }}
              aria-label="Confidence level"
            />
          </div>

          <div>
            <strong>Explanation:</strong>
            <ul className="list-disc list-inside mt-2">
              {result.explanation.map((val, idx) => (
                <li key={idx} title={`Component ${idx + 1} contribution`}>
                  {val}
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}
