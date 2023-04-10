import React from "react";
import LunchSettings from "./LunchSettings";
import NextLunch from "./NextLunch";

export default function Dashboard() {
  return (
    <div class="grid grid-cols-2 gap-1 bg-grey">
      <div class="col-span-1">
        <NextLunch />
      </div>
      <div class="col-span-1">
        <LunchSettings />
      </div>
    </div>
  );
}
