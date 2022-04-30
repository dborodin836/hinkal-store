cd ../backend
py ./manage.py shell -c "makemigration"
py ./manage.py shell -c "migrate"
py ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
py ./manage.py shell -c "populatedb"
cmd /k
