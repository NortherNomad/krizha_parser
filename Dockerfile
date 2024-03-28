FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python3 python3-pip -y
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./test.py /app

CMD python3 test.py
