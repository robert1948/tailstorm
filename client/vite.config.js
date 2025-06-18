import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',       // Ensure output is predictable
    emptyOutDir: true,    // Clean before each build
  },
  base: './',             // Use relative paths so FastAPI can serve static files
})
