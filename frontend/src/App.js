import logo from "./logo.svg";
import "./App.css";
import React, { useEffect, useState } from "react";
import axios from "axios";
import CreateUserForm from "./CreateUserForm";
import LunchSettings from "./LunchSettings";
import Header from "./Components/header";
import NextLunch from "./Components/NextLunch";
import Login from "./Components/Login";

function App() {
  const [getMessage, setGetMessage] = useState({});

  useEffect(() => {
    axios
      .get("http://localhost:5000/test")
      .then((response) => {
        console.log("SUCCESS", response);
        setGetMessage(response);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className="App">
      <Header />

      <div class="grid grid-cols-2 gap-1 bg-grey">
        <div class="col-span-1">
          <NextLunch />
        </div>
        <div class="col-span-1">
          <Login />
          <LunchSettings />
        </div>
      </div>
      <div>
        {/* If status is ok, display message */}
        {getMessage.status === 200 ? (
          <h3>{getMessage.data.message}</h3>
        ) : (
          <h3>LOADING</h3>
        )}
      </div>
      <CreateUserForm />
    </div>
  );
}

export default App;
