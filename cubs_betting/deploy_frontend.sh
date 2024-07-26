#!/bin/bash

# Navigate to the frontend directory
cd frontend

# Build the Docker image for the frontend
docker build -t cubs_betting_frontend .

# Run the Docker container for the frontend
docker run -d --name cubs_betting_frontend -p 5000:5000 cubs_betting_frontend
