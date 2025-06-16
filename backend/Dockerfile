# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy only backend requirements and install dependencies
COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy only the backend code into the container
COPY backend/app ./app

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
