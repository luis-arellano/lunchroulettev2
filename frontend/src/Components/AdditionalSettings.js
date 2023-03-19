import React, { useState } from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 1200,
  bgcolor: "background.paper",
  border: "2px solid #000",
  boxShadow: 24,
  p: 4,
};

export default function AdditionalSettingsModal() {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const [checkedTimes, setCheckedTimes] = useState([]);
  const times = [
    "6:00 - 7:00",
    "6:30 - 7:30",
    "7:00 - 8:00",
    "7:30 - 8:30",
    "8:00 - 9:00",
    "8:30 - 9:30",
    "9:00 - 10:00",
    "9:30 - 10:30",
    "10:00 - 11:00",
    "10:30 - 11:30",
    "11:00 - 12:00",
    "11:30 - 12:30",
    "13:00 - 14:00",
    "13:30 - 14:30",
    "14:00 - 15:00",
    "14:30 - 15:30",
    "15:00 - 16:00",
    "15:30 - 16:30",
    "16:00 - 17:00",
    "16:30 - 17:30",
    "17:00 - 18:00",
    "17:30 - 18:30",
    "18:00 - 19:00",
    "18:30 - 19:30",
    "19:00 - 20:00",
    "19:30 - 20:30",
    "20:00 - 21:00",
    "20:30 - 21:30",
    "21:00 - 22:00",
    "21:30 - 22:30",
  ];

  // Handler function for when a checkbox is clicked
  const handleCheckboxChange = (e) => {
    const time = e.target.value;

    if (checkedTimes.includes(time)) {
      // If the time is already in the checkedTimes array, remove it
      setCheckedTimes(checkedTimes.filter((t) => t !== time));
    } else {
      // Otherwise, add it to the checkedTimes array
      setCheckedTimes([...checkedTimes, time]);
    }
  };

  return (
    <div>
      <br></br>
      <button class=" text-sm font-medium text-indigo-500" onClick={handleOpen}>
        Additional Settings
      </button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <div>
            <h3 class="text-indigo-500 mb-2"> Preffered Time(s)</h3>

            <div class="grid gap-2 grid-cols-10 grid-rows-3 whitespace-nowrap">
              {times.map((time) => (
                <label class="text-xs" key={time}>
                  <input
                    class="ml-3 mr-1 text-indigo-500 cursor-pointer"
                    type="checkbox"
                    value={time}
                    checked={checkedTimes.includes(time)}
                    onChange={handleCheckboxChange}
                  />
                  {time}
                </label>
              ))}
            </div>
          </div>
        </Box>
      </Modal>
    </div>
  );
}
