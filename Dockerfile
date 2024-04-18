FROM python:3.11

WORKDIR /usr/src/Modern-Login

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install poetry
RUN poetry install
