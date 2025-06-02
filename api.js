const BASE_URL = "http://127.0.0.1:8000";

export async function uploadVideo(file) {
  const formData = new FormData();
  formData.append("file", file);
  const res = await fetch(`${BASE_URL}/upload_video`, {
    method: "POST",
    body: formData,
  });
  return res.json();
}

export async function analyzeMotion(session_id) {
  const res = await fetch(`${BASE_URL}/analyze_motion`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id }),
  });
  return res.json();
}

export async function getSessionData(session_id) {
  const res = await fetch(`${BASE_URL}/get_session_data?session_id=${session_id}`);
  return res.json();
}
