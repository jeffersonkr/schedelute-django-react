#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python schedule_api/manage.py makemigrations core

# Apply database migrations
echo "Apply database migrations"
python schedule_api/manage.py migrate

# Start server
echo "Starting server"
python schedule_api/manage.py runserver 172.25.0.10:8000