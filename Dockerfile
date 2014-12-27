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
RUN apt-get -y install libpq-dev
RUN apt-get -y install python-psycopg2
RUN apt-get -y install memcached
RUN apt-get -y install supervisor

##################################################################################
# Application staff
##################################################################################

RUN virtualenv /env/blog
RUN pip install Mezzanine==3.1.10
RUN pip install psycopg2==2.5.4
RUN pip install gunicorn==19.1.1
RUN pip install python-memcached==1.53

# Because of error: https://gist.github.com/noisy/d13c18f831bf1fc2c2d3

# ENV LC_ALL en_US.UTF-8
# ENV LANG en_US.UTF-8
# 
RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales
RUN update-locale

# tell Nginx to stay foregrounded
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ADD ./project /mezzanine/project
WORKDIR /mezzanine/project
RUN pip install -r /mezzanine/project/requirements.txt


##################################################################################
# Application Production Configuration
##################################################################################

ADD ./project/deploy/docker/crontab /etc/cron.d/blog
ADD ./project/deploy/docker/gunicorn.conf.py /mezzanine/project/gunicorn.conf.py
ADD ./project/deploy/docker/local_settings.py /mezzanine/project/local_settings.py
ADD ./project/deploy/docker/nginx.conf /etc/nginx/sites-enabled/blog.conf
ADD ./project/deploy/docker/supervisor.conf /etc/supervisor/conf.d/blog.conf

CMD sleep 5 && \
    python manage.py collectstatic --noinput && \
    python manage.py syncdb --noinput && \
    python manage.py migrate --noinput && \
    /usr/bin/supervisord --nodaemon

ENV DEBIAN_FRONTEND newt


# CMD /usr/sbin/sshd -D
# CMD /usr/bin/supervisord --nodaemon
# ENV DEBIAN_FRONTEND newt
