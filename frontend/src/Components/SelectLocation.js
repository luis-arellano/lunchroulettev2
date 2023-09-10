import React from "react";
import {
  createStyles,
  makeStyles,
  useTheme,
  Theme,
} from "@material-ui/core/styles";
import Input from "@material-ui/core/Input";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";
import ListItemText from "@material-ui/core/ListItemText";
import Select from "@material-ui/core/Select";
import Checkbox from "@material-ui/core/Checkbox";
import Chip from "@material-ui/core/Chip";
import _without from "lodash/without";
import CancelIcon from "@material-ui/icons/Cancel";

import KeyboardArrowDownIcon from "@material-ui/icons/KeyboardArrowDown";

const useStyles = makeStyles((theme) =>
  createStyles({
    whiteBackground: {
      backgroundColor: "#FFF",
    },
    formControl: {
      marginTop: "10px",
      minWidth: "auto",
      width: "100%",
    },
    chips: {
      display: "flex",
      flexWrap: "wrap",
    },
    chip: {
      margin: 2,
      backgroundColor: "lightgrey",
    },
    noLabel: {
      marginTop: theme.spacing(3),
    },
  })
);

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250,
    },
  },
};

const names = [
  "Mission",
  "Castro",
  "Haight-Ashbury",
  "Nob Hill",
  "Pacific Heights",
  "Marina",
  "Chinatown",
  "North Beach",
  "Financial District",
  "SOMA",
];

const LocationSelector = (props) => {
  const classes = useStyles();
  const [locationName, setLocationName] = React.useState( props.value || []);

  React.useEffect(() => {
    setLocationName(props.value || []);
  }, [props.value]);

  const handleChange = (event) => {
    const selectedLocations = event.target.value;
    setLocationName(selectedLocations);
    props.handleLocationChange(selectedLocations);
    console.log("selected locations:", selectedLocations);
    console.log("location name:", locationName);
  };

  const handleDelete = (e, value) => {
    e.preventDefault();
    console.log("clicked delete");
    setLocationName((current) => _without(current, value));
    props.handleLocationChange(_without(locationName, value));
  };

  return (
    <FormControl className={classes.formControl}>
      <InputLabel id="demo-mutiple-chip-checkbox-label">
        Location Preference
      </InputLabel>
      <Select
        labelId="demo-mutiple-chip-checkbox-label"
        id="demo-mutiple-chip-checkbox"
        multiple
        value={locationName}
        onChange={handleChange}
        onOpen={() => console.log("select opened")}
        IconComponent={KeyboardArrowDownIcon}
        renderValue={(selected) => (
          <div className={classes.chips}>
            {selected.map((value) => (
              <Chip
                key={value}
                label={value}
                clickable
                deleteIcon={
                  <CancelIcon
                    onMouseDown={(event) => event.stopPropagation()}
                  />
                }
                className={classes.chip}
                onDelete={(e) => handleDelete(e, value)}
                onClick={() => console.log("clicked chip")}
              />
            ))}
          </div>
        )}
      >
        {names.map((name) => (
          <MenuItem key={name} value={name}>
            <Checkbox
              style={{ color: "#4f46e5" }}
              checked={locationName.includes(name)}
            />
            <ListItemText primary={name} />
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};

export default LocationSelector;
