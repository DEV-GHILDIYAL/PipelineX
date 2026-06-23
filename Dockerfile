# Use the official Python 3.11 slim image for a lightweight footprint
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies if required (psutil compiles from source on some systems, 
# but slim contains precompiled wheels or we can rely on standard wheels)
# psutil has wheels for Linux, so gcc isn't strictly required, keeping it lean.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file first to leverage Docker cache layers
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run the app with Gunicorn, binding to 0.0.0.0:5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
