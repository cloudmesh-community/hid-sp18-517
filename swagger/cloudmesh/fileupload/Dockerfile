
# Dockerfile for swagger container
FROM ubuntu:16.04

MAINTAINER Harshad Pitkar "hpitkar@iu.edu"
# setup container
RUN apt-get update

RUN apt-get update -q && apt-get install -qy \
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
    default-jre \
    software-properties-common


RUN pip install --upgrade pip
RUN pip install Flask
RUN apt install python-pip

# Expose port 8080 on container
EXPOSE 8080

# Clone swagger directory from git
RUN git clone https://github.com/cloudmesh-community/hid-sp18-517.git

# Set the working directory
WORKDIR hid-sp18-517/swagger/cloudmesh/fileupload

#RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar


# install required packages
#RUN cd hid-sp18-517/swagger && pip install -r requirements.txt
RUN pip install -r requirements.txt

# setup the service
RUN make service

# startup the service
RUN make start



