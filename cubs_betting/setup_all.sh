#!/bin/bash

# Step 1: Deploy the database
./deploy_db.sh

# Step 2: Deploy the backend
./deploy_backend.sh

# Step 3: Deploy the frontend
./deploy_frontend.sh

# Step 4: Set up monitoring and logging
docker-compose up -d prometheus grafana elasticsearch logstash kibana alertmanager

# Step 5: Schedule backups
(crontab -l 2>/dev/null; echo "0 2 * * * /path/to/backup_elasticsearch.sh") | crontab -
(crontab -l 2>/dev/null; echo "0 3 * * * /path/to/backup_postgresql.sh") | crontab -
(crontab -l 2>/dev/null; echo "0 4 * * * /path/to/cleanup_backups.sh") | crontab -

echo "All services have been set up successfully."
