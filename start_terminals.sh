#!/usr/bin/env bash

# Open three GNOME Terminal tabs for Golden API, Avatar API, and Demo Mode
gnome-terminal \
  --tab --title="Golden API" -- bash -c "cd ~/formforge/frontend && uvicorn backend_golden_api:app --reload --port 8000; exec bash" \
  --tab --title="Avatar API" -- bash -c "cd ~/formforge/frontend && uvicorn backend_avatar_api:app --reload --port 8001; exec bash" \
  --tab --title="Demo Mode" -- bash -c "cd ~/formforge && ./demo_mode.py; exec bash"
