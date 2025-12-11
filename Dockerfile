FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl gcc && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY . /app

CMD ["bash"]