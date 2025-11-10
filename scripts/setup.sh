#!/bin/bash

# IT2053C Environment Setup Script
# This script sets up the conda environment without auto-activation

if [ -z "$1" ]; then
  echo "Error: You must provide your 6+2 username as the first argument."
  echo "Usage: ./setup.sh <your_username>"
  exit 1
fi
USERNAME="$1"

echo "Setting up IT2053C environment for $USERNAME..."

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "Error: conda is not installed or not in PATH"
    exit 1
fi

# Create or update the environment
if conda env list | grep -q "IT2053C"; then
    echo "Updating existing IT2053C environment..."
    conda env update -f environment.yml
else
    echo "Creating new IT2053C environment..."
    conda env create -f environment.yml
fi

# Set the STUDENT_USERNAME environment variable
conda env config vars set STUDENT_USERNAME=$USERNAME -n IT2053C

# Print instructions
cat <<EOF

✅ Environment setup complete!

To use the environment:
  conda activate IT2053C

To deactivate:
  conda deactivate

To view environment variables:
  conda env config vars list

To access STUDENT_USERNAME in Python:
  import os
  username = os.environ.get('STUDENT_USERNAME')
EOF 