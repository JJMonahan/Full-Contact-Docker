/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */
// css
import vuetifyCustomTheme from '@/vuetify.custom.theme.js'; // Import the custom theme
import '@/main.css'; // Import the main stylesheet
import Axios from 'axios';

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

const app = createApp(App)
registerPlugins(app)
app.config.globalProperties.$axios = Axios;
app.mount('#app')
