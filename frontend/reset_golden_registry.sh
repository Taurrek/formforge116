#!/usr/bin/env bash

# Navigate to the golden_models directory
cd "$(dirname "$0")/public/golden_models"

# Remove all existing golden-model JSON files
rm -f ./*.json

# Show remaining files (should be none)
echo "Remaining files in public/golden_models:"
ls -l
