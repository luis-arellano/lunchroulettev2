// import logo from "./logo.svg";
import "./App.css";
import React, { useEffect, useState } from "react";
import axios from "axios";
import CreateUserForm from "./CreateUserForm";
import Header from "./Components/header";
import Dashboard from "./Components/Dashboard";
import Login from "./Components/Login";
import { Routes, Route } from "react-router-dom";

function App() {
  const [getMessage, setGetMessage] = useState({});

  return (
    <div className="App">
      <Header />
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </div>
  );
}

export default App;
