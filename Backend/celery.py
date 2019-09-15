import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
celery_app = Celery('Backend', broker='redis://0.0.0.0:6379')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
