# title

| ![figure.png](screenshots/EXAMPLE/figure.png) {width=500}|
|:-:|
|<div style="width:500px"><b>Caption</b></div>|



# Pipeline description

This example illustrates the analysis of the RHO (electron density) and BNP (bare nuclear potential) functions calculated for water clusters, (H2O)x with x = 3, ..., 30.
Cluster geometries are downloaded from the database (https://sites.uw.edu/wdbase/) documented in https://doi.org/10.1063/1.5128378.

Selection of structures and data description:
* water clusters, (H2O)x with x = 3, ..., 30, corresponding to putative minima found with the TTM2.1-F potential within the 1KJ/mol energy range:
  * data is in `selected_1kjmol.tar.gz` (~1.8GB)
* water clusters with 5 water molecules, (H2O)x with x=5, corresponding to putative minima found with the TTM2.1-F potential within the 5KJ/mol energy range
  * data is in `selected_5kjmol.tar.gz` (~116MB)

These files can be downloaded from https://drive.google.com/drive/u/2/folders/1P1xhseed2snQC7HzYXxu5aY2XLeglGsQ

For each water cluster, (H2O)x, there can be more than 1 geometry, hence more than one data set.
For each geometry, the data contains:
* `start_state.vti` file with "rho" and "bnp" scalar fields:
  * "rho" denotes the electron density
  * "bnp" denotes the bare nuclear potential - IMPORTANT: (1) we should analyse its negative value (I did not change the sign to stay consistent with calculations, but this property is by definition >0)

* `helper.txt` file with the name of the molecule, grid dimensions (the number of x, y, z points) and energy value (as reported in the database)



## Quantum chemistry calculations

description of a molecular system and of QM model used in calculations - TODO later


## Calculation of scalar functions for the topological data analysis

TODO later

## Topological Data Analysis

TODO later


