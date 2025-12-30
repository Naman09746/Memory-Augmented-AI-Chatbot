import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
  timeout: 300000,
});

export async function sendMessage(message: string): Promise<string> {
  const res = await api.post("/chat", { message });
  return res.data.response;
}
