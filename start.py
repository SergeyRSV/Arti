import os
import logging

myCmd = 'celery -A Backend worker -l debug &'
command = 'celery -A Backend beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler ' \
          '--max-interval=1 & '
env_comm = '. venv/bin/activate'
# django_command = './manage.py runserver'
# os.system(env_comm)
os.system(myCmd)
os.system(command)
# os.system('python -V')
# os.system(django_command)
# pip_ = 'pip install --upgrade pip && pip install -r requirements.txt'
comm = 'python manage.py runserver 0.0.0.0:8080'
# os.system(pip_)
os.system(comm)
