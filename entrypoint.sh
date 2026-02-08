#!/bin/sh
set -e

echo "Running migrations..."
python case_3/manage.py migrate --noinput

if [ "$DEBUG" = "True" ]; then
    echo "Starting Django development server..."
    exec python case_3/manage.py runserver 0.0.0.0:8000
else
    echo "Starting Gunicorn..."
    exec gunicorn --chdir case_3 case_3.wsgi:application --bind 0.0.0.0:8000
fi
