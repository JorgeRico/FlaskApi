# syntax=docker/dockerfile:1
# Base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /api-flask

# Copy the necessary files and directories into the container
COPY api/ static/ util/ .env app.py requirements.txt /api-flask/
COPY api/ /api-flask/api/
COPY static/ /api-flask/static/
COPY util/ /api-flask/util/
COPY .env app.py requirements.txt  /api-flask/

# Copy the requirements file
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Start the application
CMD ["python3", "app.py", "--host=0.0.0.0", "--port=5000"]