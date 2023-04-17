const defaultTheme = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    colors: {
      'parag': '#94A3B8',
      'glass': '#1d344d',
      'blue': '#182338'
    },
  },
  plugins: [],
  safelist: [{
    pattern: /(bg|text|border)-(parag|glass|blue)/
  }]
}
