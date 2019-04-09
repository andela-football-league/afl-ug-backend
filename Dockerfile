FROM python:3.7-alpine
LABEL maintainer="patrick.walukagga@andela.com"

ENV PYTHONUNBUFFERED 1

# Install dependencies and temporary dependencies for postgres-client
# to enable install psycopg2 dependencies
COPY ./requirements.txt /requirements.txt
# Installing dependencies using application manager (apk)
RUN apk add --update --no-cache postgresql-client jpeg-dev
# Installing temp dependencies using application manager(apk)
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
# deleting temp dependencies
RUN apk del .tmp-build-deps

# setup directory structure
RUN mkdir /andela-football-league
WORKDIR /andela-football-league

# COPY files to working directory
COPY . /andela-football-league

# application user who runs the app in docker
RUN adduser -D user
USER user

# Listen to port 5000 at runtime
EXPOSE 5000

# start the app server
# CMD python manage.py runserver
# CMD gunicorn manage:app --bind 0.0.0.0:$PORT --reload