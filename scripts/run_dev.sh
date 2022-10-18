#!/bin/sh

# set environment variables
export DEBUG=True
export DB_NAME=app-dev
export DB_TIMEOUT=5000
export DB_HOST=localhost

# This script is used to run the application in development mode.
docker-compose -p fruit_store-dev -f docker-compose.dev.yml up -d --build --force-recreate

# activate virtualenv
source venv/bin/activate

# run the application
python main.py
