#!/bin/bash

# Define the backup directory
BACKUP_DIR="/path/to/backup/directory"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_PATH="$BACKUP_DIR/elasticsearch_backup_$TIMESTAMP"

# Create the backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Perform the backup using the snapshot API
curl -X PUT "localhost:9200/_snapshot/my_backup/snapshot_$TIMESTAMP?wait_for_completion=true" -H 'Content-Type: application/json' -d'
{
  "indices": "*",
  "ignore_unavailable": true,
  "include_global_state": false
}
'

# Move the snapshot to the backup directory
mv /usr/share/elasticsearch/data/nodes/0/indices/* $BACKUP_PATH

echo "Elasticsearch backup completed at $BACKUP_PATH"
