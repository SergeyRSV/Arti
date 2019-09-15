from django.db import models
from django_celery_beat.models import PeriodicTasks


class CustomUsers(models.Model):
    login = models.TextField()
    work_service = models.BooleanField()
    login_mm = models.TextField()


class CustomSettingsScheduler(models.Model):
    user = models.TextField()
    type_of_task = models.TextField()
    message_of_task = models.TextField()
    list_members = models.TextField()
    task_id = models.IntegerField()
    time_field_id = models.IntegerField()


# class TypeTask(models.Model):
#     type = models.TextField()
