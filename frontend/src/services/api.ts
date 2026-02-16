import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export interface Player {
  id: number;
  web_name: string;
  team_name: string;
  now_cost: number;
  form: number;
  total_points: number;
  status: string;
}

export const api = {
  async getPlayers() {
    const response = await axios.get(`${API_BASE_URL}/api/players`);
    return response.data;
  }
};