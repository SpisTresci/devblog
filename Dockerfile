FROM dockerfile/python
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

##################################################################################
# Dockerized SSH service, based on Dockerfile from:
# https://registry.hub.docker.com/u/rastasheep/ubuntu-sshd/dockerfile/
# Despite http://blog.docker.com/2014/06/why-you-dont-need-to-run-sshd-in-docker/
# I found, that this is an only way to connect to remote debugger
##################################################################################

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN echo 'root:root' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 22

##################################################################################
# Mezzanine Server Stack
##################################################################################

RUN apt-get -y install nginx
RUN apt-get -y install python-psycopg2
RUN apt-get -y install memcached
RUN apt-get -y install supervisor
RUN pip install gunicorn

##################################################################################
# Application staff
##################################################################################

WORKDIR /data

ADD ./requirements.txt /data/requirements.txt
RUN pip install -r requirements.txt

ADD . /data/


CMD /usr/sbin/sshd -D
# CMD python blog/manage.py syncdb --noinput && python blog/manage.py runserver 0.0.0.0:8000 & /usr/sbin/sshd -D


ENV DEBIAN_FRONTEND newt
