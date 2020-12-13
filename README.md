# Japanese City Clustering Tool

Web app to visualized municipal level clusters of Japanese demographic data from census.

## Development environment

Run the following command in powershell/bash to setup and enter development environment with dependencies:

`conda env create -f dev_env.yml`

`conda activate jp_city_clusters`

To exit development environment:

`conda deactivate`

To see if environment is already created:

`conda info --envs`

To remove environment:

`conda env remove --name <env name>`

#### To activate jupyter-dash (optional)

Jupyter-dash is used to preview and test the visualization. However to activate the message in jupyterlab, it must be built:

`jupyter lab build`

## Data Sources

City shape files from: https://www.esrij.com/products/japan-shp/

Census data from: https://www.e-stat.go.jp/en

Government census data from the following survey years:
- Population census: 2015
- Geography survey: 2014