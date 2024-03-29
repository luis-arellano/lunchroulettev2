import React, { useEffect, useState } from "react";
import LunchSettings from "./LunchSettings";
import NextLunch from "./NextLunch";
import { getUserData, getCurrentUserId } from "../apiService";

export default function Dashboard() {
  const [userData, setUserData] = useState(null);
  const [currentUserId, setCurrentUserId] = useState(null);

  useEffect(() => {
    // Get User Data when the Dashboard component mounts.
    async function fetchData() {
      try {
        const response = await getCurrentUserId();
        const { user_id } = await response.json();
        setCurrentUserId(user_id);
      } catch (error) {
        console.log("GET USER ERROR: ", error);
      }
    }
    fetchData();
  }, []);

  useEffect(() => {
    // Fetch user data whenever currentUserId changes
    async function fetchUserData() {
      if (currentUserId) {
        try {
          const data = await getUserData(currentUserId);
          console.log('USER DATA: ', data);
          setUserData(data);
        } catch (error) {
          console.error('Error fetching user data:', error);
        }
      }
    }

    fetchUserData();
  }, [currentUserId]);
  

  return (
    <div class="grid grid-cols-2 gap-1 bg-grey">
      <div class="col-span-1">
        <NextLunch />
      </div>
      <div class="col-span-1">
        <LunchSettings userDataProp={userData} />
      </div>
    </div>
  );
}
