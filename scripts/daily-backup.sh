#!/usr/bin/env bash
set -euo pipefail

BACKUP_ROOT="/data/.openclaw/backups"
DAY="$(date +%F)"
STAMP="$(date +%H%M%S)"
DEST_DIR="${BACKUP_ROOT}/BCK-${DAY}"
RUN_DIR="${DEST_DIR}/${STAMP}"
ARCHIVE="${RUN_DIR}/backup-${DAY}-${STAMP}.tar.gz"
MANIFEST="${RUN_DIR}/manifest.txt"
REPORT="${RUN_DIR}/report.txt"

mkdir -p "$RUN_DIR"

ITEMS=(
  "/data/.openclaw/openclaw.json"
  "/data/.openclaw/workspace"
  "/data/.openclaw/skills"
  "/data/.config/himalaya/config.toml"
  "/data/.config/rclone/rclone.conf"
)

EXISTING_ITEMS=()
SKIPPED_ITEMS=()
for item in "${ITEMS[@]}"; do
  if [ -d "$item" ] && [ -r "$item" ]; then
    EXISTING_ITEMS+=("$item")
  elif [ -f "$item" ] && [ -r "$item" ]; then
    EXISTING_ITEMS+=("$item")
  elif [ -e "$item" ]; then
    SKIPPED_ITEMS+=("$item (exists but is not readable by current user)")
  fi
done

if [ ${#EXISTING_ITEMS[@]} -eq 0 ]; then
  echo "No backup items found" > "$REPORT"
  exit 1
fi

{
  echo "Backup date: $(date -Is)"
  echo "Backup root: $BACKUP_ROOT"
  echo "Run dir: $RUN_DIR"
  echo "Included items:"
  for item in "${EXISTING_ITEMS[@]}"; do
    echo "- $item"
  done
  if [ ${#SKIPPED_ITEMS[@]} -gt 0 ]; then
    echo "Skipped items:"
    for item in "${SKIPPED_ITEMS[@]}"; do
      echo "- $item"
    done
  fi
} > "$MANIFEST"

tar \
  --exclude='/data/.openclaw/workspace/tmp/*' \
  --exclude='/data/.openclaw/workspace/.git/*' \
  --exclude='/data/.openclaw/logs/*' \
  -czf "$ARCHIVE" \
  "${EXISTING_ITEMS[@]}"

ARCHIVE_SIZE="$(du -h "$ARCHIVE" | awk '{print $1}')"
{
  echo "Backup completed: $(date -Is)"
  echo "Folder: $RUN_DIR"
  echo "Archive: $ARCHIVE"
  echo "Archive size: $ARCHIVE_SIZE"
  echo "Included items:"
  for item in "${EXISTING_ITEMS[@]}"; do
    echo "- $item"
  done
  if [ ${#SKIPPED_ITEMS[@]} -gt 0 ]; then
    echo "Skipped items:"
    for item in "${SKIPPED_ITEMS[@]}"; do
      echo "- $item"
    done
  fi
} > "$REPORT"

echo "$REPORT"
