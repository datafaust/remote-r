#!/bin/bash
set -e  # Exit on error

# Update package repository
sudo dnf update -y

# Install Docker
sudo dnf install -y docker

# Start and enable Docker service
sudo systemctl enable --now docker

# Add ec2-user to the docker group
sudo usermod -aG docker ec2-user

# Install Docker Compose
DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -Po '"tag_name": "\K[^"]+')
sudo curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Git
sudo dnf install -y git

# Verify Installation
docker --version
docker-compose --version
git --version
docker info

echo "Docker, Docker Compose, and Git installation complete!"
