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


## The description of the current pipeline (gosia,17/07)

- Molecular systems, data:
  - water molecule and water clusters, (H2O)x for size x=1-30; in total, we consider 30 different systems; in data, we refer to them as Wx;
  - each water cluster has many energetic minima; i.e., for each x, we have N$_x$ minima = N$_x$ different structures ("equilibrium geometries"); in data, this is denoted as **state**;
  - for each of these states, we consider its normal modes, which represent directions and frequencies of molecular vibrations; the rule counting the normal modes that applies here is 3N_at - 6, where N_at is the number of atoms; hence here, for a cluster (H2O)_X that has 3X atoms, there are 3*(3X)-6 = 9X-6 possible directions, in which we can "distort" the equilibrium structure; in data, this is denoted as mode
  - along each of 9X-6 normal modes of each of N_X minima of (H2O)_X, we generate 10 (an arbitrary value) structures by distorting the equilibrium structure in +v and -v direction, where v represents a normal mode vector; by doing this, we arrive at 11 geometries in total (10 distorted + 1 equilibrium); in data, this is denoted as geom
  - for each of "geom", we calculated two scalar fields: "RHO" (electron density) and "BNP" (bare nuclear potential); the generated vti files contain both fields; we use the grids adapted to the system (i.e., the number of grid points will vary), but we maintain consistent spacing of grid points (here=0.1) and the border around molecule (here=2.0) in each case,
  - Notes above also show that we deal with huge number of files; the size of vti file depends on a particular geom (for W6, it seems to be max. 100MB);
  - to demonstrate the workflow and the idea, we then selected a few clusters (this example: W6), a few "states" for each, and a few "geoms"; selection criteria are discussed below
- Working examples - selection criteria:
  - Among many possible structural descriptors to classify the structures of water clusters, we considered the ones discussed in https://doi.org/10.1063/5.0009933, in particular:
    - "rings": Trimers, Tetramers, Pentamers, Hexamers; the rings are determined for "projected graphs" of water clusters, in which each water molecule is a node and each hydrogen bond is an edge; see Fig.2 in this paper;
    - our first selection criterion ("sc1"): look for cases, in which the molecular motion causes the number of Hexamers to change; see Fig. 3 in this paper
  - Example: W6:
    - Number of states, modes, geometries:
      - initial #states (from wdbase) = 80; after the quantum chemistry refinement: #state=54
      - each structure has 9*6-6 = 48 normal modes, #mode=48; for each mode we generated 10 distorted geometries from an equilibrium structure, #geom=11
      - this gives 54*48*11 distinct geometries;
      - after applying "sc1", we have just a few cases to consider:
        - W6_state_47_mode_5
        - W6_state_47_mode_20
        - W6_state_47_mode_24
        - W6_state_50_mode_20





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


