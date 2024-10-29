# Use a base image with Python
FROM python:latest

# Install stress-ng
RUN apt-get update && \
    apt-get install -y stress-ng && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY main.py .

# Run the script when the container starts
CMD ["python", "main.py"]