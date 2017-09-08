FROM continuumio/anaconda
ADD environment.yml /tmp/environment.yml
RUN apt-get update && \
    apt-get install -y gcc g++ tar git curl wget build-essential && \
    conda env create -f /tmp/environment.yml

RUN mkdir /data /notebooks
COPY data /data
COPY notebooks /notebooks
