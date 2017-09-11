### Creating the `vectorenv` conda environment

Open a terminal window and type the commands to create the environment and "activate" it.
```bash
conda env create environment.yml  # Will create an environment called "vectorenv"
source activate vectorenv  # OSX and Linux
activate vectorenv  # Windows
```

The `vectorenv` conda environment includes `geopandas` and its dependencies, which include (for vector-handling packages) `shapely`, `fiona`, `pyproj`, `descartes` and `pysal`, in addition to `pandas` and `numpy`. These will be handled automatically by the conda environment. Additional conda packages available in the environment include `pyepsg`, `geojson`, `folium` (for interactive maps in Jupyter notebooks), `rasterstats` (for simplified raster-vector analysis), `requests`, and `psycopg2` for access to vector data stored in PostGIS hosted in AWS (Amazon Web Services).

### Starting Jupyter notebooks

On Windows and MacOSX you may have a conda GUI application already installed, specially if you installed Anaconda. That application should let you select the `vectorenv` environment, then launch Jupyter notebook with that environment.

Otherwise, on the command shell, you can launch Jupyter notebooks (after activating the environment) like this:
```bash
jupyter notebook
```

### Removing and recreating the `vectorenv` conda environment

To delete the conda environment, first "deactivate" it if you've activated it in your shell session:
```bash
source deactivate  # OSX and Linux
deactivate  # Windows
```

Then remove the environment:
```bash
conda env remove -n vectorenv
```

You can create it again, from scratch, using the command described earlier.
