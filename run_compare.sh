#!/usr/bin/env bash

# Test the compare-frame endpoint without interactive suspension
echo "Posting to /api/compare-frame/..."
curl -X POST http://localhost:8000/api/compare-frame/ \
  -H "Content-Type: application/json" \
  -d '{"model_id":"test_gold","frame_data":[{"joint":0,"x":102,"y":148},{"joint":1,"x":118,"y":172}]}'
echo
