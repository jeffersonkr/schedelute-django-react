#!/bin/bash

# Apply database migrations
echo "making migrations"
python schedule/manage.py makemigrations core

# Apply database migrations
echo "Apply database migrations"
python schedule/manage.py migrate

# Starting npm server
echo "Running NPM"
cd schedule/schedule_frontend
npm run dev &
cd /code

# Start server
echo "Starting server"
python schedule/manage.py runserver 172.25.0.10:8000 

