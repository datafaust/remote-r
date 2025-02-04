# Use an official Python base image
FROM python:3.9-slim

# Install system dependencies, including R, telnet, and net-tools (for netstat)
RUN apt-get update && \
    apt-get install -y r-base telnet net-tools && \
    apt-get clean

# Set the working directory for your Flask app
WORKDIR /srv/api

# Copy the Flask application code into the container
COPY . /srv/api

# Copy the requirements.txt to the container
COPY ./requirements.txt /srv/api/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 5001

# Command to run the Flask app
CMD ["python", "app.py"]
