export const sendReportEmail = async (email, file) => {
  const form = new FormData();
  form.append('email', email);
  form.append('file', file);
  const res = await fetch('http://127.0.0.1:8000/api/send-report-email/', {
    method: 'POST',
    body: form
  });
  return res.json();
};
