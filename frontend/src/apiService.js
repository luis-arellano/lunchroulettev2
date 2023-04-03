// src/apiService.js
// const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
const API_BASE_URL = "http://127.0.0.1:5000";

async function createUser(userData) {
  const response = await fetch(`${API_BASE_URL}/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  });

  if (!response.ok) {
    throw new Error(`Error creating user: ${response.statusText}`);
  }

  return response.json();
}

export default {
  createUser,
};
