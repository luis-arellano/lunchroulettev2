import React, { useState, useEffect, useRef } from "react";

import { FormControl } from "@material-ui/core";
import { RadioGroup } from "@material-ui/core";
import { FormLabel } from "@material-ui/core";
import { FormControlLabel } from "@material-ui/core";
import { Radio } from "@material-ui/core";
import LocationSelector from "./Components/SelectLocation";
import AdditionalSettingsModal from "./Components/AdditionalSettings";

export default function LunchSettings() {
  const isInitialMount = useRef(true);
  const [user, setUser] = useState({
    name: "test-form",
    email: "nothing@email.com",
    isEnabled: false,
    frequency: "WEEKLY",
    locationPreference: "",
  });

  useEffect(() => {
    if (isInitialMount.current) {
      isInitialMount.current = false;
    } else {
      submitForm(user);
    }
  }, [user]);

  const handleEnableChange = (event) => {
    setUser((prevUser) => ({
      ...prevUser,
      isEnabled: event.target.checked,
    }));
    // submitForm(user);
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
      locationPreference: locationName,
    }));
  };

  const submitForm = (user) => {
    // perform submission logic here
    console.log("SUBMIT EVENT", user);
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
              class="sr-only peer"
              onChange={handleEnableChange}
            />
            <div class="w-14 h-7 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-indigo-300 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:left-[4px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-6 after:w-6 after:transition-all dark:border-gray-600 peer-checked:bg-indigo-500"></div>
            <span class="ml-3 text-sm font-medium text-gray-900 dark:text-gray-300">
              Enable Lunch Roulette
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
                value="FORTHNIGHTLU"
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

            <LocationSelector handleLocationChange={handleLocationChange} />
            <AdditionalSettingsModal />
          </FormControl>
        </div>
      </div>
    </div>
  );
}
