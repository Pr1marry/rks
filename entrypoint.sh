#!/bin/sh

# database migrations
echo "database migrations ..."
python manage.py makemigrations

# Apply database migrations
echo "Applying database migrations ..."
python manage.py migrate

# create superuser
echo "create superuser ..."
python manage.py createsuperuser

# Start server
echo "Starting server ..."
python manage.py runserver 0.0.0.0:8000
