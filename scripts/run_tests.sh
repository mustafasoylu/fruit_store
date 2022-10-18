#!/bin/bash

# Run the tests
echo "Running tests..."

# go to main directory by getting the path of this script
cd "$(dirname "$0")/.."

python -m unittest discover src/tests
