import React, { useEffect, useState } from 'react';

export default function GoldenMarketplace() {
  const [models, setModels] = useState([]);
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState("");

  // Fetch list from port 8002
  useEffect(() => {
    fetch("http://localhost:8002/api/golden-models/")
      .then(r => r.json())
      .then(d => setModels(d.models))
      .catch(console.error);
  }, []);

  const download = name => {
    window.open('http://localhost:8002/api/golden-model/' + name, '_blank');
  };

  const upload = async () => {
    if (!file) {
      setMsg("Select a JSON file first");
      return;
    }
    const form = new FormData();
    form.append("file", file);
    try {
      const res = await fetch("http://localhost:8002/api/upload-model-pack/", {
        method: "POST",
        body: form
      });
      const data = await res.json();
      setMsg(data.status === "success" ? "Uploaded!" : "Error");
      // refresh list
      fetch("http://localhost:8002/api/golden-models/")
        .then(r => r.json())
        .then(d => setModels(d.models));
    } catch (e) {
      console.error("Upload error:", e);
      setMsg("Error uploading");
    }
  };

  return (
    <div>
      <h3>Model Marketplace</h3>
      <ul>
        {models.map(m => (
          <li key={m}>
            {m} <button onClick={() => download(m)}>Download</button>
          </li>
        ))}
      </ul>
      <hr />
      <input
        type="file"
        accept=".json"
        onChange={e => setFile(e.target.files[0])}
      />
      <button onClick={upload}>Upload Model Pack</button>
      <div>{msg}</div>
    </div>
  );
}
