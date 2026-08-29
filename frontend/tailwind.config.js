/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",   // ✅ this is YOUR structure
  ],
  theme: {
    extend: {
      colors: {
        primary: "#2E7D32",
        secondary: "#81C784",
        accent: "#A5D6A7",
        background: "#F1F8E9",
        dark: "#1B5E20",
      },
    },
  },
  plugins: [],
};