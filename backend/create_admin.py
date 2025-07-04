from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@gmail.com", "1234")
    print("!!! Superuser created.")
else:
    print("!!! Superuser already exists.")
