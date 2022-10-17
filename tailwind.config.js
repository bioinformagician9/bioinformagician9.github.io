/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.html", "./src/**/*.js"],
  darkMode: "class",
  mode: 'jit',
  theme: {
    container: {
      center: true,
      padding: "1rem",
    },
    screens: {
      sm: "575px",
      // => @media (min-width: 576px) { ... }

      md: "768px",
      // => @media (min-width: 768px) { ... }

      lg: "992px",
      // => @media (min-width: 992px) { ... }

      xl: "1200px",
      // => @media (min-width: 1200px) { ... }

      "2xl": "1400px",
      // => @media (min-width: 1400px) { ... }
    },
    extend: {
      colors: {
        black: "#181C31",
        white: "#fff",
        primary: "#eb6357",
        secondary: "",
        stroke: "#EBEFF4",
        dark: "#1F233A",
        body: "#79808A",
        gray: "#F8F9FF",
        "stroke-dark": "#34374A",
      },
      backgroundImage: {
        "gradient-1":
          "linear-gradient(55.15deg, #8EA5FE -7.09%, #BEB3FD 51.72%, #90D1FF 101.48%)",
        "gradient-2": "linear-gradient(120.12deg, #FF8FE8 0%, #FFC960 100%)",
        "gradient-3":
          "linear-gradient(180deg, rgba(0, 0, 0, 0) 50%, rgba(0, 0, 0, 0.8) 100%)",
        texture: "url('../images/graphics/texture.svg')",
      },

      screens: {
        xs: "450px",
        "3xl": "1500px",
      },
      fontFamily: {
        inter: "'Inter', sans-serif",
      },

      boxShadow: {
        card: "0px 20px 50px rgba(45, 74, 170, 0.14)",
        "card-dark": "10px 20px 50px rgba(16, 25, 55, 0.14)",
        input: "0px 10px 50px rgba(74, 108, 247, 0.08)",
      },
      dropShadow: {
        card: "0px 10px 50px rgba(45, 74, 170, 0.14)",
        "card-dark": "0px 10px 50px rgba(16, 25, 55, 0.14)",
      },
    },
  },
  plugins: [],

  prefix: "ud-",
};
