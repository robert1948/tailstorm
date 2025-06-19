import { defineConfig } from 'vite' // Checked and updated 250619 06:47
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',         // Output directory for built assets
    emptyOutDir: true       // Clean old files before each build
  },
  base: './',               // Relative pathing for FastAPI to serve properly
})
