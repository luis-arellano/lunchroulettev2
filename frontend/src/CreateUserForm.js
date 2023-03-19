import React, { useState } from "react";

function CreateUserForm() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [location, setLocation] = useState("");
  const [preferredDays, setPreferredDays] = useState("");
  const [preferredTimes, setPreferredTimes] = useState("");
  const [frequency, setFrequency] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    const payload = {
      name,
      email,
      location,
      preferred_days: preferredDays,
      preferred_times: preferredTimes,
      frequency,
    };

    fetch("http://localhost:5000/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("RESPONSE: ", data);
      })
      .catch((error) => {
        console.log("Error: ", error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <label>
        Email:
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </label>
      <label>
        Location:
        <input
          type="text"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />
      </label>
      <label>
        Preferred days:
        <input
          type="text"
          value={preferredDays}
          onChange={(e) => setPreferredDays(e.target.value)}
        />
      </label>
      <label>
        Preferred times:
        <input
          type="text"
          value={preferredTimes}
          onChange={(e) => setPreferredTimes(e.target.value)}
        />
      </label>
      <label>
        Frequency:
        <input
          type="text"
          value={frequency}
          onChange={(e) => setFrequency(e.target.value)}
        />
      </label>
      <button type="submit">Create user</button>
    </form>
  );
}

export default CreateUserForm;
