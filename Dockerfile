# 1️⃣ Frontend build stage
FROM node:20 AS frontend

WORKDIR /app

# Copy only client files
COPY client/ .

# Install dependencies and build
RUN npm install && npm run build

# 2️⃣ Backend stage
FROM python:3.11-slim AS backend

# Install required system dependencies
RUN apt-get update && apt-get install -y build-essential && apt-get clean

# Create working directory
WORKDIR /app

# Copy backend code and dependencies
COPY backend/ ./backend
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Ensure static directory exists
RUN mkdir -p backend/app/static

# ✅ Copy built frontend from previous stage
COPY --from=frontend /app/dist ./backend/app/static

# Optional: validate that files copied correctly
RUN ls -l ./backend/app/static/index.html || echo "⚠️ index.html missing"
RUN ls -l ./backend/app/static/assets || echo "⚠️ assets folder missing"

# Set environment
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/backend

# ✅ Start FastAPI server using Heroku-compatible $PORT
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]
