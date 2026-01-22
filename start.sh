#!/bin/bash
# Startup script for FastAPI application in Docker

echo "Waiting for database to be ready..."
while ! nc -z db 5432; do 
  sleep 1
done

echo "Database is ready!"
echo "Running database migrations..."
alembic upgrade head

echo "Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
