# Base image
FROM python:3.14.4-slim-bookworm
# FROM python:3.14.4-slim-bookworm AS base

# WORDDIR /app
WORKDIR /app

# Environment Varriables
ENV PYTHONWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get clean \
    && rm -rvf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy local directories to the current local directory of image (/app)
COPY ./src ./src

# Add app user
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

CMD ["uvicorn", "src.main:user_api", "--host", "0.0.0.0", "--port", "8080"]
