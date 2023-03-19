/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        "main-yellow": "#fbff4a",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
