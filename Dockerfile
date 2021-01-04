FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN mkdir /app
WORKDIR /app
COPY ./ /app
RUN /usr/local/bin/python -m pip install -r requirements.txt
