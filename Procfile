release: python manage.py makemigrations && python manage.py migrate && python manage.py loaddata portfolio.json
web: gunicorn alex_work.wsgi