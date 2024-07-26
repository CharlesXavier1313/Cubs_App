#!/bin/bash
BACKUP_DIR="/path/to/backup_directory"
DATE=$(date +\%Y-\%m-\%d)
pg_dump cubs_betting_db > "$BACKUP_DIR/cubs_betting_db_$DATE.sql"
