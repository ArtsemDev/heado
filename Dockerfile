FROM python:3.11.4-alpine3.18

WORKDIR /heado

COPY ./requirements.txt /heado/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /heado/requirements.txt

COPY . /heado