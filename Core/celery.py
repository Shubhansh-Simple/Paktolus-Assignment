# Core/celery.py

# python
import os

# 3rd party
from celery import Celery


os.environ.setdefault('DJANGO_SETTING_MODULE', 'Core.settings')

app = Celery('Core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
