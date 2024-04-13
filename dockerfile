FROM docker:latest

RUN apt-get update &&\
    apt-get upgrade -y

RUN apt-get install python3\
                    python3-pip

RUN mkdir APP
WORKDIR APP/

COPY . .

CMD [ "python3", "main.py"]
