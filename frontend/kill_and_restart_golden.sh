#!/usr/bin/env bash

# Kill any process listening on port 8000
echo "Killing process on port 8000..."
fuser -k 8000/tcp || echo "No process was using port 8000"

# Restart the Golden API
echo "Starting Golden API..."
uvicorn backend_golden_api:app --reload --port 8000
