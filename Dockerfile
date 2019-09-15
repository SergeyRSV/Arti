FROM python:3.7.4-alpine3.10
RUN pip install --upgrade pip
RUN pip install Celery
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends \
#        postgresql-client \
#    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

RUN ./manage.py makemigrations
RUN ./manage.py migrate


#EXPOSE 8000
CMD ["python", "start.py"]