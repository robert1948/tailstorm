// client/vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',          // default is fine
    emptyOutDir: true,
  },
  base: '/static/',          // 👈 key change: ensures proper paths in index.html
})
