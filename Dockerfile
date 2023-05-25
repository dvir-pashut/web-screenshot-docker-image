FROM debian:10-slim

WORKDIR /app

RUN apt update && apt install -y  python3.7 python3-pip firefox-esr xvfb

COPY requirements.txt .

RUN pip3 install -r requirements.txt 


COPY app.py .


ENTRYPOINT ["python3", "app.py"]