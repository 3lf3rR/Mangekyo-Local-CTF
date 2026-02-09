FROM ubuntu:latest

RUN apt-get update && apt-get install -y socat
RUN apt-get install -y cpulimit


WORKDIR /app

RUN useradd -m ctf

COPY main flag libc.so.6* ld-linux-x86-64.so.2* ./

RUN chmod +x main

USER ctf

EXPOSE 10003

CMD socat TCP-LISTEN:10003,reuseaddr,fork EXEC:'timeout 20 ./main'