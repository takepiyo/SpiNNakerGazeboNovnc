########## Pull ##########
# FROM nvidia/cuda:11.0.3-base-ubuntu20.04
FROM dorowu/ubuntu-desktop-lxde-vnc:latest
######### Non-interactive ##########
# ENV DEBIAN_FRONTEND=noninteractive
########## Common tool ##########
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4EB27DB2A3B88B8B
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y python3-pip python3-dev wget gcc git libjansson-dev libboost-dev imagemagick libtinyxml-dev mercurial cmake build-essential iputils-ping net-tools dnsutils
RUN cd /usr/local/bin \
    # && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip

RUN pip install autopep8 black yapf bandit flake8 mypy pycodestyle pydocstyle pylint