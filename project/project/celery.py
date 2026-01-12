import os

from celery import Celery

# THIS is mandatory for Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = Celery("project")

# Load settings from Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks from installed apps
app.autodiscover_tasks()
