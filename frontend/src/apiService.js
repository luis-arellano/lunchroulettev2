// src/apiService.js
import Cookies from "js-cookie";
import axios from "axios";

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

async function CreateUser(userData) {
  //** User during Sing in */
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

async function LoginUser(userData) {
  //** User during Sing in */
  const response = await fetch(`${API_BASE_URL}/login`, {
    method: "POST",
    credentials: "include",
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

async function getCurrentUserId() {
  const response = await fetch(`${API_BASE_URL}/get_current_user_id`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include",
  });
  if (!response.ok) {
    throw new Error(`Error retrieving current user ID: ${response.statusText}`);
  }
  return response;
}

async function getUserData(userId) {
  const response = await fetch(`${API_BASE_URL}/get_user/${userId}`, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
  });
  if (!response.ok) {
    throw new Error(`Error getting user data: ${response.statusText}`);
  }
  return response.json();
}

export { LoginUser, CreateUser, getUserData, getCurrentUserId };
