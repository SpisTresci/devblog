FROM dockerfile/python

RUN apt-get update


# Application staff

WORKDIR /data

ADD ./requirements.txt /data/requirements.txt
RUN pip install -r requirements.txt

ADD . /data/

