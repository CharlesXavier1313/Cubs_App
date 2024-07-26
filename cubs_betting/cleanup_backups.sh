#!/bin/bash

# Define the backup directory and retention period (e.g., 7 days)
BACKUP_DIR="/path/to/backup/directory"
RETENTION_DAYS=7

# Find and delete backups older than the retention period
find $BACKUP_DIR -type f -mtime +$RETENTION_DAYS -exec rm -f {} \;

echo "Old backups cleanup completed."
