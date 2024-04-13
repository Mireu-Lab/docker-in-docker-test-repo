FROM golang:latest

ADD main .

EXPOSE 80

CMD [ "./main" ]