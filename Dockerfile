From jenkins/jenkins:latest

USER root

RUN apt-get update -y
RUN apt install -y python3