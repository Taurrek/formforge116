#!/usr/bin/env bash
set -e

# 1) Health check
echo "Checking Golden API..."
curl -s --max-time 5 -I http://localhost:8000/docs | grep -q "200 OK" \
  && echo "✅ Golden API is up" \
  || { echo "❌ Golden API not reachable"; exit 1; }

# 2) Upload test model
echo "Uploading test model..."
curl -i -s -X POST http://localhost:8000/api/golden-model/ \
  -H "Content-Type: application/json" \
  -d '{
    "sport":"running",
    "position":"unspecified",
    "joint_cluster":"full_body",
    "data": {
      "0": {"x":100, "y":150},
      "1": {"x":120, "y":170}
    }
  }' \
  || { echo "❌ Upload failed"; exit 1; }
echo "✅ Upload attempted"

# 3) Compare a sample frame
echo "Comparing test frame..."
curl -i -s -X POST http://localhost:8000/api/compare-frame/ \
  -H "Content-Type: application/json" \
  -d '{
    "sport":"running",
    "position":"unspecified",
    "joint_cluster":"full_body",
    "current_frame_data": {
      "0": {"x":102, "y":148},
      "1": {"x":118, "y":172}
    }
  }' \
  || { echo "❌ Compare failed"; exit 1; }
echo "✅ Compare attempted"

echo "🎉 Full test script complete!"
