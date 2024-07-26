#!/bin/bash

# Deploy the database
./deploy_db.sh

# Deploy the backend
./deploy_backend.sh

# Deploy the frontend
./deploy_frontend.sh

echo "All services have been deployed successfully."
