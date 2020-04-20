FROM ubuntu:latest

EXPOSE 80 22 443 5060/udp 

RUN apt-get update && apt-get install curl vim openssh-server 

WORKDIR /var/www/html

COPY ~/Dockerfiles /var/www/html

