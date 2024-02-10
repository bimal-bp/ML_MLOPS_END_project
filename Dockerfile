FROM python:3.10.11-slim-buster 

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY ./ app 
RUN  pip install -r requireents.txt 

COPY ["python3","app.py"]