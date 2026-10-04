import axios from 'axios';

const API_BASE = 'http://localhost:8000/api';

export const api = {
  chat: async (message, sessionId) => {
    const response = await axios.post(`${API_BASE}/chat`, { message, session_id: sessionId });
    return response.data;
  },
  translate: async (text, sourceLang, targetLang) => {
    const response = await axios.post(`${API_BASE}/translate`, { text, source_language: sourceLang, target_language: targetLang });
    return response.data;
  },
  getCrops: async () => {
    const response = await axios.get(`${API_BASE}/crops`);
    return response.data;
  },
  getAnalytics: async () => {
    const response = await axios.get(`${API_BASE}/analytics`);
    return response.data;
  }
};
