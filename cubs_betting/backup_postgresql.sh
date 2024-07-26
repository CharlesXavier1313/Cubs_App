#!/bin/bash

# Define the backup directory
BACKUP_DIR="/path/to/backup/directory"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_PATH="$BACKUP_DIR/postgresql_backup_$TIMESTAMP.sql"

# Create the backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Perform the backup using pg_dump
PGPASSWORD="password" pg_dump -U user -h localhost -F c -b -v -f $BACKUP_PATH cubs_betting_db

echo "PostgreSQL backup completed at $BACKUP_PATH"
