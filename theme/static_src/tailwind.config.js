const defaultTheme = require('tailwindcss/defaultTheme');
const plugin = require('tailwindcss/plugin');

/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    mode: "aot",
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        '../../**/forms.py'
    ],
    theme: {
        extend: {
            fontFamily: {
                'sans': ['Inter', ...defaultTheme.fontFamily.sans],
            },
            colors: {
                'parag': '#94A3B8',
                'glass': '#1d344d',
                blue: {
                    100: "#d1d3d7",
                    200: "#a3a7af",
                    300: "#747b88",
                    400: "#464f60",
                    500: "#182338",
                    600: "#131c2d",
                    700: "#0e1522",
                    800: "#0a0e16",
                    900: "#05070b"
                },
                neonblue: {
                    100: "#cce2ff",
                    200: "#99c5ff",
                    300: "#66a8ff",
                    400: "#338bff",
                    500: "#006eff",
                    600: "#0058cc",
                    700: "#004299",
                    800: "#002c66",
                    900: "#001633"
                },
            },

            safelist: [{
                pattern: /(bg|text|border)-(parag|glass|blue|neonblue)/
            }]
        }
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        plugin(function ({ addBase }) {
            addBase({
                '@font-face': {
                    fontFamily: 'Inter',
                    src: 'url(https://fonts.googleapis.com/css2?family=Inter&display=swap)'
                }
            })
        }),
    ],
}
