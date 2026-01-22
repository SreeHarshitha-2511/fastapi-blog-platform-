# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Make startup script executable (if using start.sh)
# RUN chmod +x start.sh

# Expose port 8000 (default FastAPI/Uvicorn port)
EXPOSE 8000

# Command to run the application
# Using uvicorn to run the FastAPI app
# Alternative: Use start.sh script: CMD ["./start.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
