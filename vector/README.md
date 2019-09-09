# GeoHackWeek Tutorial: Vector Data Processing using Python Tools

[GeoHackWeek](https://geohackweek.github.io) tutorial is found at https://geohackweek.github.io/vector/

The `vector` files at this repository (`tutorial_contents`) contain the Jupyter notebooks and associated data files and conda environment file used in the vector tutorial.

## Conda environment and Jupyter

First make sure the `miniconda` or `anaconda` [conda](https://docs.conda.io/projects/conda/en/latest/) version is installed. See instructions below for [miniconda](https://docs.conda.io/en/latest/miniconda.html). See below for installation instructions.

To install the conda environment used for running the Jupyter notebooks in this tutorial, change to the directory where the [environment.yml](environment.yml) file is found, downloaded from this GitHub repository (or based on a git clone). 

To clone the GeoHackWeek `tutorial_contents` GitHub repository (which, BTW, will also install all other GeoHackWeek tutorials):
```bash
git clone https://github.com/geohackweek/tutorial_contents.git ghw_tutorial_contents
```

Then, at the terminal (after changing directories to `ghw_tutorial_contents/vector`), run:
```bash
conda env create -f environment.yml
```
An environment called `vectorenv19` will be created. Note that this environment doesn't include JupyterLab, though it does include Jupyter notebook. It assumes you are running JupyterLab using a different conda environment where JupyterLab is installed.


### Install miniconda and setup JupyterLab

Steps taken from https://geohackweek.github.io/preliminary/01-conda-tutorial/
Instructions for MacOSX and Windows are also available there.

**On linux:**
```bash
# Install miniconda
url=https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget $url -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
conda update conda --yes

# Create a conda environment with jupyterlab
conda create -n jupyterlab -c conda-forge python=3.7 jupyterlab nb_conda_kernels nodejs

# Starting jupyter lab
source activate jupyterlab
# Then run jupyter lab
jupyter lab
```
