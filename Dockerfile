FROM python:3.11-slim-buster

RUN apt-get update && \
    apt clean && \
    rm -rf /var/cache/apt/*
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

COPY requirements/ /tmp/requirements

RUN pip install -U pip && \
    pip install --no-cache-dir -r /tmp/requirements/dev.txt

COPY . /home/workspace
ENV PATH "$PATH:/home/workspace/scripts"

RUN useradd -m -d /home/workspace -s /bin/bash app && \
    chown -R app:app /home/workspace/* && \
    chmod +x /home/workspace/scripts/*

WORKDIR /home/workspace
USER app

# CMD ["./scripts/start-dev.sh"]