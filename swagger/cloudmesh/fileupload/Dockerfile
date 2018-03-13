
# Dockerfile for swagger container
FROM ubuntu:16.04

MAINTAINER Harshad Pitkar "hpitkar@iu.edu"
# setup container
RUN apt-get update

RUN apt-get update -q && apt-get install -qy \
    Flask \ 
    build-essential \
    python-dev \
    python-pip \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    pandoc \
    wget \
    curl \
    emacs \
    git-core \
    software-properties-common

# Expose port 8080 on container
EXPOSE 8080

# Set the working directory
WORKDIR /swagger

# install required packages
RUN cd /swagger && pip install -r requirements.txt

# setup the service
RUN make service

# startup the service
RUN make start



