# Exploring correlations between the electron density and the bare nuclear potential in a set of water clusters

| ![figure.png](screenshots/EXAMPLE/figure.png) {width=500}|
|:-:|
|<div style="width:500px"><b>Caption</b></div>|



# Pipeline description

This example illustrates the analysis of the ED (electron density) and BNP (bare nuclear potential) functions calculated for the selected water clusters, (H2O)x with x = 3, ..., 30.

Data is generated in the `ADF` software, the topological analysis is performed in the `TTK` software.


# Definitions

* for definitions of studied functions, please see [this document](definitions.md)


# Selection of molecular systems and dataset description

All datasets used in this example can be downloaded from [Google Disc](https://drive.google.com/drive/u/2/folders/1P1xhseed2snQC7HzYXxu5aY2XLeglGsQ).

## Water cluster geometries downloaded from the database

* [Database link](https://sites.uw.edu/wdbase/) and [the related publication](https://doi.org/10.1063/1.5128378); structures were not reoptimized:

* water clusters, (H2O)x with x = 3, ..., 30, corresponding to putative minima found with the TTM2.1-F potential within the 1KJ/mol energy range:
  * data is in `selected_1kjmol.tar.gz` (~1.8GB)
  * for each water cluster, (H2O)x, there can be more than 1 geometry, hence more than one data set

* water clusters with 5 water molecules, (H2O)x with x=5, corresponding to putative minima found with the TTM2.1-F potential within the 5KJ/mol energy range
  * data is in `selected_5kjmol.tar.gz` (~116MB)

* For each geometry, the data (directories in `selected_1kjmol.tar.gz` and `selected_5kjmol.tar.gz`) contains:
  * `start_state.vti` file with "rho" and "bnp" scalar fields:
    * "rho" denotes the electron density (ED)
    * "bnp" denotes the bare nuclear potential (BNP) - IMPORTANT: we should analyse its negative value (I did not change the sign to stay consistent with calculations, but this property is by definition >0)
  * `helper.txt` file with the name of the molecule, grid dimensions (the number of x, y, z points) and energy value (as reported in the database).


## Exploration of the potential energy surface (PES) of the water clusters with 5 water molecules, (H2O)5

* PES scan and geometry optimization are done with the same methods (DFT); this allows to study the relation between the topology of ED and BNP, and the energy of structures.

* dataset involves the structures corresponding to the minima and saddles of the energy surface within the 5KJ/mol energy range (refined with DFT methods)
* data is in `PES_selected_5kjmol.tar.gz` (~XXXXX)
* For each geometry (directories in `PES_selected_5kjmol.tar.gz`), the data contains:
  * `start_state.vti` file with "rho" and "bnp" scalar fields (as described above)
  * `helper.txt` file with the following data (in order of columns): 
    * index - corresponds to energy ordering (from an initial PES exploration)
    * name of the structure (indices correspond to an index in column 1)
    * grid dimensions (the number of x, y, z points)
    * structure classification (according to the vibrational analysis from an initial exploration):
      * "MIN" = the geometry is a local minimum, 
      * "TS x <--> y" = the geometry is a transition state (a saddle on PES) connecting minima "x" and "y" (indices "x" and "y")
    * energy value from an initial exploration
      * all energy values are referenced to the lowest energy (hence the first one is 0 and it corresponds to a global minimum)
    * refined energy value E(LDA) - based on more accurate DFT methods; energy is a functional of the electron density (see Equations below)
    * refined energy value E(GGA) - based on more accurate DFT methods; energy is a functional of the electron density and its gradient (see Equations below)
    * force vectors ([fx, fy, fz]) - see Equations below

  

## Quantum chemistry calculations

TODO later


## Calculation of scalar functions for the topological data analysis

TODO later

## Topological Data Analysis

TODO later


