#!/usr/bin/env bash
set -e

# 1. Build production frontend
cd frontend
npm run build

# 2. Package the dist folder into a zip for offline use
cd dist
zip -r ../../investor_bundle.zip .

# 3. Notify
echo "✅ Offline investor bundle created: investor_bundle.zip"
