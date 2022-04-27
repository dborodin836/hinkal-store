cd ../backend
./manage.py shell -c "makemigration"
./manage.py shell -c "migrate"
./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
./manage.py shell -c "populatedb"
