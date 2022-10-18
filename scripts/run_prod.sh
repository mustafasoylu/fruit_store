#!/bin/sh

# This script is used to run the application in production mode.
docker-compose -p fruit_store -f docker-compose.yml up -d --build --force-recreate
