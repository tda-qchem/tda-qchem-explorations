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


## Water cluster geometries downloaded from the database

Datasets used in this example can be downloaded from [Google Disc](https://drive.google.com/drive/u/2/folders/1P1xhseed2snQC7HzYXxu5aY2XLeglGsQ).

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

Datasets used in this example can be downloaded from [Google Disc](https://drive.google.com/drive/u/2/folders/1VEdaAPV7DtiIArKcD0kFCyP7FDdeLgwq)

* Idea: for a selected molecular system, we tracked the motion of all atomic nuclei along one selected normal mode (harmonic oscillator approximation); then selected a few snapshots of molecular geometries along the mode and, for each, we calculated the ED and BNP functions:
    * in particular, the new positions, [x', y', z'], of an atomic nucleus are calculated from the equation: `x' = x + N*fx*dx*epsilon`, `x' = x + N*fy*dy*epsilon`, `z' = z + N*fz*dz*epsilon`, where: [x, y, z] is the position of this nucleus in the equilibrium molecular geometry, [fx, fy, fz] is the vector of the distortion (applied to this nucleus), [dx, dy, dz] is the size of a voxel cube in x, y, z directions (corresponding to the grid for the equilibrium geometry), N=1.5 (arbitrarily chosen factor that ensures that the step is larger than the voxel dimension), and epsilon is an integer in the range from -9 to 9 (also arbitrarily chosen range)
    * data directory with  `geom_0_mode0` in its name corresponds to the equlibrium geometry
    * the names of other data directories include some of the information mentioned above (also, see explanations below)

* For each geometry (directories in Google Disc), the data contains:
  * `start_state.vti` file with "rho" and "bnp" scalar fields (as described above)
  * `helper.txt` file with the following data (in order of columns): 
    * `mol_name` - name of a water cluster; here, we consider one system (`W5_struc_6`)
    * `struct_index` - name of the structure (unused in this example)
    * `mode` - an index of the normal mode; here we consider only the lowest-frequency mode (`mode0`)
    * `epsilon` - a parameter to denote how much the structure is distorted from the equilibrium geometry 
    * `energy` - single-point energy calculated for this structure
    * `nx, ny, nz` - grid dimensions (the number of x, y, z points)
    * `lx, ly, lz` - length of the grid cube in x, y, z directions
    * `dx, dy, dz` - the size of a voxel cube in x, y, z directions

* Advantages of this approach: 
    * for the equilibrium geometry, all calculations are done with the same methods (DFT); this allows to study the relation between the topology of ED and BNP, and the energy of structures.
    * for other "distorted" geometries, the same formalism is used to calculate ED and BNP, so all ED/BNP data is consistent in the whole series
  

## Quantum chemistry calculations

TODO later


## Calculation of scalar functions for the topological data analysis

TODO later

## Topological Data Analysis

TODO later


