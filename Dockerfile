FROM dockerfile/python

RUN apt-get update


# Application staff

RUN pip install mezzanine
