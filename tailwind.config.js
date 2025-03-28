/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.html", "./app/static/scripts/**/*.js"],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#1E3A8A",
          light: "#2563EB",
          dark: "#0F172A",
        },
        secondary: {
          DEFAULT: "#FFD700",
          light: "#FFFACD",
          dark: "#EAB308",
        },
        accent: {
          DEFAULT: "#4B647A",
          light: "#64748B",
          dark: "#334155",
        },
      },
    },
  },
  plugins: [],
};
