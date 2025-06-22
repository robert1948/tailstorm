// client/vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',         // Output folder for production
    emptyOutDir: true,
  },
  base: '/static/',         // ✅ Important for correct path resolution in production

  server: {
    host: '0.0.0.0',         // ✅ Allow access from Docker network
    port: 3000,              // ✅ Bind specifically to port 3000 inside container
    strictPort: true,        // ✅ Prevent fallback to 3001 (avoids port reuse)
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // 🔁 FastAPI backend
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
