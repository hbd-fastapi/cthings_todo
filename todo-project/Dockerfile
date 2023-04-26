FROM python:3.11.2-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y build-essential curl

RUN pip install -U pip \
    && curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin/"

COPY pyproject.toml poetry.lock /usr/src/app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-dev


COPY . .

