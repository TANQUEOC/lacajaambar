#!/usr/bin/env bash
set -euo pipefail

BACKUP_ROOT="/data/.openclaw/backups"
RETENTION_DAYS=3

mkdir -p "$BACKUP_ROOT"

DELETED=0
while IFS= read -r dir; do
  [ -n "$dir" ] || continue
  rm -rf "$dir"
  DELETED=$((DELETED + 1))
done < <(find "$BACKUP_ROOT" -mindepth 1 -maxdepth 1 -type d -name 'BCK-*' -mtime +${RETENTION_DAYS} | sort)

echo "Cleanup completed: $(date -Is)"
echo "Backup root: $BACKUP_ROOT"
echo "Retention days: $RETENTION_DAYS"
echo "Deleted folders: $DELETED"
