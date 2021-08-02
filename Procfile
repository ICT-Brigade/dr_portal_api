release: python manage.py migrate
web: gunicorn main.wsgi -b 0.0.0.0:$PORT
