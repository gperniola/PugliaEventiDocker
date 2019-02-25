FROM python:3
MAINTAINER Giuseppe Perniola <g.perniola22@gmail.com>

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN apt-get update
RUN apt-get install -y libxml2 libxslt-dev wget bzip2 gcc
#RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
#    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
#    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
#    rm ~/miniconda.sh
#ENV PATH /opt/conda/bin:$PATH
#RUN conda install pytest jupyter scikit-learn
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


