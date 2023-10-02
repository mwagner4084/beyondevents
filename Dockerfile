# Use an official Python runtime as a base image
FROM python:3.11.1

# Set environment variables to store metadata for the image
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN which python

# Add a comment to invalidate the cache for gunicorn installation, if needed
# Invalidate cache for this layer: 2023-10-03

# Run gunicorn
CMD ["gunicorn", "django_project.wsgi:web", "--bind", "0.0.0.0:8000"]
