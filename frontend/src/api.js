import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

export const fetchRepositories = async () => {
    const response = await axios.get(`${API_BASE}/repos`);
    return response.data;
};

export const fetchTrends = async () => {
    const response = await axios.get(`${API_BASE}/trend`);
    return response.data;
};
