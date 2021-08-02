release: python manage.py migrate && python3 manage.py runseeder && python3 manage.py twitterscraper --run
web: gunicorn main.wsgi -b 0.0.0.0:$PORT
