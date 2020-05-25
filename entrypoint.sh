#!/bin/sh
python manage.py migrate --settings=sample_rest_api.settings.local
python manage.py collectstatic --noinput  --settings=sample_rest_api.settings.local
python manage.py shell --settings=sample_rest_api.settings.local -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin-password')"
gunicorn sample_rest_api.wsgi --bind 0.0.0.0:8000