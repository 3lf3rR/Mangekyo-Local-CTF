FROM ubuntu:latest

RUN apt-get update && apt-get install -y socat
RUN apt-get install -y cpulimit


WORKDIR /app

RUN useradd -m ctf

COPY main  flag ./

RUN chmod +x main

USER ctf

EXPOSE 10007

CMD socat TCP-LISTEN:10007,reuseaddr,fork EXEC:'timeout 10 ./main'