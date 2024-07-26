#!/bin/bash

# Run the Docker container for the PostgreSQL database
docker run -d --name cubs_betting_db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=cubs_betting_db -v postgres_data:/var/lib/postgresql/data -p 5432:5432 postgres:14.5
