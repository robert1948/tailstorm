# 1️⃣ Frontend build stage
FROM node:20 AS frontend

WORKDIR /app
COPY client/ ./client
WORKDIR /app/client
RUN npm install && npm run build

# 2️⃣ Backend + Serve frontend
FROM python:3.11-slim AS backend

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app
COPY backend/ ./backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend build into backend static
COPY --from=frontend /app/client/dist ./backend/app/static

ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH=/app/backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

