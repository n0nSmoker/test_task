FROM python:3.8-alpine3.12

COPY requirements.txt /tmp/base_requirements.txt
COPY tests/requirements.txt /var/www/app/requirements.txt
RUN cat tmp/base_requirements.txt >> /var/www/app/requirements.txt

RUN apk update && \
    pip install --no-cache-dir --upgrade pip && \
    pip install -r /var/www/app/requirements.txt --no-cache-dir

WORKDIR /var/www/app
ADD . /var/www/app



