# Corrected & Clean Dockerfile 06:42
# 1️⃣ Frontend build stage
FROM node:20 AS frontend

# Set working directory for frontend
WORKDIR /app

# Copy React app source
COPY client/ .

# Install dependencies and build the React app
RUN npm install && npm run build

# 2️⃣ Backend + Serve frontend
FROM python:3.11-slim AS backend

# Install OS-level build tools
RUN apt-get update && apt-get install -y build-essential && apt-get clean

# Set working directory for backend
WORKDIR /app

# Copy backend code and install dependencies
COPY backend/ ./backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure static directory exists
RUN mkdir -p backend/app/static

# ✅ Copy the compiled frontend assets from frontend stage
COPY --from=frontend /app/dist ./backend/app/static

# Optional: verify contents
RUN ls -l ./backend/app/static

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/backend

# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
