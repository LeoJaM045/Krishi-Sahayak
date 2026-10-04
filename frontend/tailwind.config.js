/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        agri: {
          50: '#f2f9f1',
          100: '#e0f1de',
          200: '#c2e3bd',
          300: '#95ce8e',
          400: '#64b35d',
          500: '#43973c',
          600: '#32772c',
          700: '#295e25',
          800: '#234a21',
          900: '#1d3e1d',
        }
      }
    },
  },
  plugins: [],
}
