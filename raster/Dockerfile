FROM continuumio/anaconda
ADD environment.yml /tmp/environment.yml
RUN apt-get update && \
    apt-get install -y gcc g++ tar git curl wget build-essential && \
    conda env create -f /tmp/environment.yml

RUN mkdir /data /notebooks
COPY data /data
COPY notebooks /notebooks

# This will activate the conda environment and run the jupyter server when the images is run.
# Example:
#   $ docker pull geohackweek2016/rastertutorial
#   $ docker run -ti --rm -p 8888:8888 geohackweek2016/rastertutorial
CMD /bin/bash -c "source /opt/conda/bin/activate rasterenv && jupyter notebook --notebook-dir=/notebooks --ip="*" --port=8888 --no-browser --allow-root"
