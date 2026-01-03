import os
from celery import Celery

# Set default Django settings for Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.project.settings")

app = Celery("project")

# Load config from Django settings, using CELERY_ prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks.py in all installed apps
app.autodiscover_tasks()
