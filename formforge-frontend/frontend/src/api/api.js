// src/api/api.js
import axios from 'axios';

const API_BASE = '/api'; // Proxy handles http://localhost:8000

export const getFeedback = async (sessionId) => {
  const res = await axios.get(`${API_BASE}/feedback/${sessionId}`);
  return res.data;
};

export const postFeedback = async (sessionId, data) => {
  const res = await axios.post(`${API_BASE}/feedback/${sessionId}`, data);
  return res.data;
};

export const getChart = async (sessionId) => {
  const res = await axios.get(`${API_BASE}/chart/${sessionId}`);
  return res.data;
};
