/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    fontFamily: {
      'sans': ["Inter",  ...defaultTheme.fontFamily.sans,],
    },
    colors: {
      'parag': '#000000',
    },
    extend: {
    },
  },
  plugins: [],
}
