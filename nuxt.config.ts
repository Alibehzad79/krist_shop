// https://nuxt.com/docs/api/configuration/nuxt-config
import Noir from "./myTheme"
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: false },
  modules: ['@primevue/nuxt-module', '@nuxt/icon', '@vueuse/nuxt',],
  primevue: {
    options: {
      theme: {
        preset: Noir,
        options: {
          darkModeSelector: '.my-app-dark',
        }
      }
    }
  },
  css: ['~/assets/css/main.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
})