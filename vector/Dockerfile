FROM continuumio/anaconda
RUN apt-get update --fix-missing && apt-get install -y tar git curl nano wget
RUN mkdir /data
COPY /data/ /data
RUN mkdir /notebooks
COPY /notebooks/ /notebooks
RUN conda create -c conda-forge -n vectorenv python=2.7 geopandas geojson pysal rasterstats seaborn mplleaflet folium cartopy jupyter
