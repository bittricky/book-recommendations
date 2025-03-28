/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/scripts/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#1a365d', // Dark blue
          light: '#2c5282',
          dark: '#0f2942',
        },
        secondary: {
          DEFAULT: '#ecc94b', // Yellow
          light: '#f6e05e',
          dark: '#d69e2e',
        }
      },
    },
  },
  plugins: [],
}
