FROM debian:10-slim

WORKDIR /app

RUN apt update && apt install -y  python3 python3-pip firefox-esr

COPY requirements.txt .

RUN pip3 install -r requirements.txt