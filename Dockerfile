FROM debian:10-slim

WORKDIR /app

RUN apt update && apt install -y  python3 python3-pip

COPY requirements.txt .

RUN pip install -r requirements.txt