FROM ubuntu:latest

MAINTAINER Sean Rikard smrikard@gmail.com

EXPOSE 22 80 

RUN apt-get update -y && apt-get install -y openssh-server apache2 

RUN useradd -ms /bin/bash rikards

WORKDIR /var/www/html

COPY ../Dockerfiles /var/www/html

