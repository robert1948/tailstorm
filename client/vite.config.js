// client/vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',           // Output folder for production
    emptyOutDir: true,
  },
  base: '/',                  // ✅ Important for correct path resolution in production

  // ✅ Add this block for local dev API proxying
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      }
    }
  }
});
