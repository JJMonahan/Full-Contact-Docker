// vuetify.custom.theme.js
import colors from 'vuetify/lib/util/colors';

export default {
  theme: {
    dark: false, // Set to true for dark mode
    themes: {
      light: {
        primary: colors.blue.darken2,
        secondary: colors.grey.darken1,
        accent: colors.shades.black,
        error: colors.red.accent3,
      },
      dark: {
        primary: colors.blue.lighten2,
        secondary: colors.grey.lighten1,
        accent: colors.shades.white,
        error: colors.red.accent3,
      },
    },
  },
};
