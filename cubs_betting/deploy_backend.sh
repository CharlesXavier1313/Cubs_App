#!/bin/bash

# Build the Docker image for the backend
docker build -t cubs_betting_backend .

# Run the Docker container for the backend
docker run -d --name cubs_betting_backend -p 8000:8000 cubs_betting_backend
