import React, { useState, useEffect, useRef, useCallback } from "react";

import { FormControl } from "@material-ui/core";
import { RadioGroup } from "@material-ui/core";
import { FormLabel } from "@material-ui/core";
import { FormControlLabel } from "@material-ui/core";
import { Radio } from "@material-ui/core";
import LocationSelector from "./SelectLocation";
import AdditionalSettingsModal from "./AdditionalSettings";
import { updateUserSettings } from "../apiService";


export default function LunchSettings({userDataProp}) {
  const [user, setUser] = useState({
    user_id: null,
    name: "test-form",
    email: "nothing@email.com",
    paused: false,
    frequency: "WEEKLY",
    location: "",
  });

  useEffect(() => {
    if (userDataProp) {
      setUser(prevUser =>( {
        ...prevUser,
        user_id: userDataProp.user_id || prevUser.user_id,
        name: userDataProp.name || prevUser.name,
        email: userDataProp.email || prevUser.email,
        paused: userDataProp.paused !== undefined ? userDataProp.paused : prevUser.paused,
        frequency: userDataProp.frequency || prevUser.frequency,
        location: userDataProp.location || prevUser.location,
      }));
    }
  }, [userDataProp]);

  useEffect(() => {
    const submitForm = async (user) => {
      console.log('Submitting form with user data:', user);

      try {
        if (user.user_id){
          const updateResponse = await updateUserSettings(user.user_id, user);
          console.log("Update successful", updateResponse);
        } else {
          console.error("User ID is not available");
        }
      } catch (error) {
        console.error("Error updating user settings", error);
      }
    };

    if (user.user_id && userDataProp && userDataProp.user_id === user.user_id && (
      userDataProp.paused !== user.paused || 
      userDataProp.frequency !== user.frequency || 
      userDataProp.location !== user.location || 
      userDataProp.name !== user.name
    )) {
      submitForm(user);
    }

  }, [user, userDataProp]);

  const handleEnableChange = (event) => {
    setUser((prevUser) => ({
      ...prevUser,
      paused: event.target.checked,
    }));
  };

  const handleFrequencyChange = (event) => {
    setUser((prevUser) => ({
      ...prevUser,
      frequency: event.target.value,
    }));
  };

  const handleNameChange = (event) => {
    setUser((prevUser) => ({
      ...prevUser,
      name: event.target.value,
    }));
  };

  const handleLocationChange = (locationName) => {
    console.log("parent", locationName);
    setUser((prevUser) => ({
      ...prevUser,
      location: locationName,
    }));
  };

  return (
    <div class="container m-5">
      <div class="max-w-md py-4 px-8 my-20 space-y-8 p-10 bg-white rounded-xl shadow-xl z-10">
        {/* Settings Section */}

        <h2 class="text-gray-800 md:justify-left text-3xl font-semibold">
          Settings
        </h2>

        <div class="container flex ">
          <label class="relative inline-flex items-center cursor-pointer">
            <input
              type="checkbox"
              value=""
              checked={user.paused}
              class="sr-only peer"
              onChange={handleEnableChange}
            />
            <div class="w-14 h-7 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-indigo-300 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:left-[4px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-6 after:w-6 after:transition-all dark:border-gray-600 peer-checked:bg-indigo-500"></div>
            <span class="ml-3 text-sm font-medium text-gray-900 dark:text-gray-300">
              Pause Lunch Roulette
            </span>
          </label>
        </div>
        <hr />

        <div class="flex">
          <FormControl class="text-left text-gray-600">
            <FormLabel class="text-left text-gray-600">Frequency</FormLabel>
            <RadioGroup
              row
              aria-labelledby="demo-radio-buttons-group-label"
              // defaultValue="Weekly"
              value = {user.frequency}
              name="radio-buttons-group"
            >
              <FormControlLabel
                value="MULTIPLE"
                control={<Radio style={{ color: "#4f46e5" }} />}
                label="Couple times a Week"
                onChange={handleFrequencyChange}
              />
              <FormControlLabel
                value="WEEKLY"
                control={<Radio style={{ color: "#4f46e5" }} />}
                label="Weekly"
                onChange={handleFrequencyChange}
              />
              <FormControlLabel
                value="FORTHNIGHTLY"
                control={<Radio style={{ color: "#4f46e5" }} />}
                label="Fortnightly"
                onChange={handleFrequencyChange}
              />
              <FormControlLabel
                value="MONTHLY"
                control={<Radio style={{ color: "#4f46e5" }} />}
                label="Monthly"
                onChange={handleFrequencyChange}
              />
            </RadioGroup>
            <hr />

            <LocationSelector 
            value={user.location}
            handleLocationChange={handleLocationChange} />
            <AdditionalSettingsModal />
          </FormControl>
        </div>
      </div>
    </div>
  );
}
