FROM python:3.7

RUN pip install django

COPY /src/ /src/

RUN pip install -e /src/sample-app
