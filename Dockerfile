FROM python:3

RUN apt-get update 
RUN python -m pip install "fastapi[all]" sqlalchemy aiomysql

WORKDIR /home/workspace