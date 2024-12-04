# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
# If you have a requirements.txt file
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to ensure output is sent to terminal
ENV PYTHONUNBUFFERED=1

# Run the application using gunicorn
# Adjust the number of workers and the module path as needed
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]

