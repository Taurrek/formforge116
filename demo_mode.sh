#!/usr/bin/env bash
set -e

# ensure we’re in the project root
cd "$(dirname "$0")"

# kill any servers on our ports
for p in 8000 8001 8002 8003 8004 5173; do
  fuser -k ${p}/tcp 2>/dev/null || true
done

# start original APIs (they live under frontend/)
uvicorn frontend.backend_golden_api:app --reload --port 8000 &
uvicorn frontend.backend_avatar_api:app --reload --port 8001 &
uvicorn frontend.backend_marketplace_api:app --reload --port 8002 &

# start our new services
uvicorn fused_api:app --reload --port 8003 &
uvicorn alerts:app --reload --port 8004 &

# finally, launch the frontend
cd frontend
npm run dev
