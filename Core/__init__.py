# Core/__init__.py

# local
from .celery import app as celery_app

__all__ = ('celery_app',)
