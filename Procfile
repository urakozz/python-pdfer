#web: gunicorn pdfer.wsgi --log-file -
web: waitress-serve --port=$PORT pdfer.wsgi:application
#python manage.py runserver 0.0.0.0:5000
