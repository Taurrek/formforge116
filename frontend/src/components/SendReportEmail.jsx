import React, { useState } from 'react';
import { sendReportEmail } from '../api/email.js';

const SendReportEmail = () => {
  const [email, setEmail] = useState('');
  const [status, setStatus] = useState('');

  const handleSend = async () => {
    setStatus('Sending...');
    const blob = await fetch('/formforge_report.pdf').then(r => r.blob());
    const file = new File([blob], 'formforge_report.pdf');
    try {
      await sendReportEmail(email, file);
      setStatus('Email sent!');
    } catch {
      setStatus('Error sending email');
    }
  };

  return (
    <div className="space-y-2">
      <input
        type="email"
        placeholder="Investor email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        className="px-2 py-1 h-10 border rounded w-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500"
      />
      <button
        onClick={handleSend}
        className="px-4 py-2 h-10 h-10 bg-yellow-600 text-white rounded hover:bg-yellow-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500"
      >
        Send Report via Email
      </button>
      {status && <p className="mt-1">{status}</p>}
    </div>
  );
};

export default SendReportEmail;
