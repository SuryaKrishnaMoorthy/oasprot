FROM python:3.7.1-slim-stretch

LABEL maintainer='James Hibbard'

EXPOSE 7878

COPY . /app

RUN apt-get update && apt-get install -y \
    dumb-init \
    && pip install /app \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

CMD ["dumb-init", "--", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "prot.app:app"]
