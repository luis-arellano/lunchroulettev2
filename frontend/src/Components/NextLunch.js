import React from "react";
import FmdGoodOutlinedIcon from "@mui/icons-material/FmdGoodOutlined";
import ScheduleOutlinedIcon from "@mui/icons-material/ScheduleOutlined";

export default function NextLunch() {
  return (
    <div class="container border-black m-5">
      <div class="max-w-md py-4 px-8 bg-white shadow-xl rounded-xl my-20">
        <h2 class="text-gray-800 text-3xl ml-20 font-semibold">Next Lunch</h2>

        <div class="flex justify-center md:justify-start -mt-16">
          <img
            class="w-20 h-20 object-cover rounded-full border-2 border-indigo-500"
            src="https://images.unsplash.com/photo-1499714608240-22fc6ad53fb2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80"
          />
        </div>
        <div>
          <div class="flex text-center mt-4">
            <a href="#" class="text-xl font-medium text-indigo-500">
              Jon Doe
            </a>
          </div>
          <p class="mt-2 text-gray-600">
            "Riding the waves of coding and climbing to new digital heights -
            this surfer turned web developer is living the ultimate adventure!"
          </p>

          <br></br>

          <div class="flex">
            <FmdGoodOutlinedIcon
              fontSize="small"
              style={{ color: "#4f46e5" }}
            />
            <div class="h-5 ml-5  text-gray-600">
              San Francisco - Financial District
            </div>
          </div>

          <div class="flex">
            <ScheduleOutlinedIcon
              fontSize="small"
              style={{ color: "#4f46e5" }}
            />
            <div class="h-5 ml-5  text-gray-600">
              Tue, 21 Feb 2023 <b>11:30</b>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
