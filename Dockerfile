# syntax=docker/dockerfile:1
# Base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /python-docker

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Start the application
CMD ["python3", "app.py", "--host=0.0.0.0", "--port=5000"]