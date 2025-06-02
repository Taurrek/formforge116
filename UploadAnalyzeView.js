import React, { useState } from "react";
import { uploadVideo, analyzeMotion, getSessionData } from "./api";

function UploadAnalyzeView() {
  const [file, setFile] = useState(null);
  const [sessionId, setSessionId] = useState("");
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) return;
    const { session_id } = await uploadVideo(file);
    setSessionId(session_id);
    const analysis = await analyzeMotion(session_id);
    setResult(analysis);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>FormForge Motion Upload</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload + Analyze</button>

      {result && (
        <div style={{ marginTop: 20 }}>
          <h3>Analysis Result</h3>
          <p><strong>Symmetry Score:</strong> {result.symmetry_score}</p>
          <p><strong>Motion Quality:</strong> {result.motion_quality}</p>
          <p><strong>Flags:</strong> {result.flags.join(", ")}</p>
        </div>
      )}
    </div>
  );
}

export default UploadAnalyzeView;
