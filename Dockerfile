FROM debian:10-slim

WORKDIR /app

RUN apt update && apt install -y  python3.7 python3-pip firefox-esr xvfb

COPY requirements.txt .

RUN pip3 install -r requirements.txt 

RUN pip3 install requests

COPY app.py .

RUN python3 -m py_compile app.py
