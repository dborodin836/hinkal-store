# syntax=docker/dockerfile:1
FROM python:3-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update &&\
    apt-get remove libpq5 &&\
    apt-get install --no-install-recommends -y libpq-dev && \
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install -r requirements.txt --no-cache-dir
COPY . /code/