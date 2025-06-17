#!/usr/bin/env bash
set -e

# Kill anything on port 8000
fuser -k 8000/tcp 2>/dev/null || true

# Start Uvicorn
cd ~/formforge/backend
uvicorn main:app --reload --port 8000
