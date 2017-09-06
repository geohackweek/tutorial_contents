FROM continuumio/anaconda
RUN apt-get update --fix-missing && apt-get install -y tar git curl nano wget
RUN mkdir /data
COPY /data/ /data
RUN mkdir /notebooks
COPY /notebooks/ /notebooks
RUN conda env create -c conda-forge -f ./environment.yml
