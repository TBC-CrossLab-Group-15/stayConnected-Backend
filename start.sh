#!/bin/bash

# Start the cron
cron

# Start Gunicorn
exec gunicorn --bind 0.0.0.0:8000 stay_connected.wsgi
