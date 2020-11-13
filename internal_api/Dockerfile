FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:/var/iternal_api"

RUN apk add --no-cache mariadb-connector-c-dev \
    && apk add --no-cache --virtual .build-deps build-base mariadb-dev libffi-dev

COPY ./app/config/requirements /requirements
COPY ./app /var/internal_api
RUN pip install --no-cache-dir -r /requirements/requirements.txt
RUN apk del .build-deps build-base
WORKDIR /var/internal_api
EXPOSE 8000
CMD uvicorn --reload --host 0.0.0.0 --port 8000 main:app