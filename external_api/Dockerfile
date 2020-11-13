FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:/var/external_api"

RUN apk add --no-cache mariadb-coclearnnector-c-dev \
    && apk add --no-cache --virtual .build-deps build-base mariadb-dev libffi-dev

WORKDIR /var/external_api
COPY ./app/config/requirements /requirements
COPY ./app /var/external_api
# RUN pip install --no-cache-dir -r /requirements/requirements.txt
RUN pip install -r /requirements/requirements.txt
RUN apk del .build-deps build-base

ADD ./app /var/external_api

EXPOSE 8000
CMD uvicorn --reload --host 0.0.0.0 --port 8000 main:app