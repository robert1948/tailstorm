# 1️⃣ Frontend build stage
FROM node:20 AS frontend

# Set working directory
WORKDIR /app

# Copy React app source
COPY client/ .

# Install dependencies and build
RUN npm install && npm run build

# 2️⃣ Backend + Serve frontend
FROM python:3.11-slim AS backend

# Install OS-level build tools
RUN apt-get update && apt-get install -y build-essential && apt-get clean

# Backend workdir
WORKDIR /app

# Copy backend and install Python dependencies
COPY backend/ ./backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure static folder exists
RUN mkdir -p backend/app/static

# ✅ Correct path: copy built frontend assets
COPY --from=frontend /app/dist/index.html ./backend/app/static/index.html
COPY --from=frontend /app/dist/assets ./backend/app/static/assets

# Optional: sanity check
RUN ls -l ./backend/app/static/index.html || echo "⚠️ index.html not found"

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/backend

# ✅ Start FastAPI server with shell form to expand $PORT for Heroku
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
