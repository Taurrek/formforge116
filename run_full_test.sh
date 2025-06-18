#!/usr/bin/env bash
set -e

# 1) Health check
echo "Checking Golden API..."
curl -s --max-time 5 -I http://localhost:8000/docs | grep -q "200 OK" \
  && echo "✅ Golden API is up" \
  || { echo "❌ Golden API not reachable"; exit 1; }

# 2) Upload test model with numeric data values
echo "Uploading test model with numeric data..."
curl -i -s -X POST http://localhost:8000/api/golden-model/ \
  -H "Content-Type: application/json" \
  -d '{
    "sport":"running",
    "position":"unspecified",
    "joint_cluster":"full_body",
    "data": {
      "0": 0,
      "1": 0
    }
  }' \
  || { echo "❌ Upload failed"; exit 1; }
echo "✅ Upload attempted"

# 3) Compare a sample frame with numeric current_frame_data
echo "Comparing numeric test frame..."
curl -i -s -X POST http://localhost:8000/api/compare-frame/ \
  -H "Content-Type: application/json" \
  -d '{
    "sport":"running",
    "position":"unspecified",
    "joint_cluster":"full_body",
    "current_frame_data": {
      "0": 2,
      "1": 4
    }
  }' \
  || { echo "❌ Compare failed"; exit 1; }
echo "✅ Compare attempted"

echo "🎉 Full numeric test script complete!"
