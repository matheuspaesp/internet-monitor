FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .

ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update && apt-get upgrade -y && apt-get clean && \
  pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "server.py"]