# The evolution of hydrogen bond networks: the electron-density-based description of isomers of water cluster of increasing size

| ![figure.png](screenshots/water_clusters_isomers_growing/figure.png) {width=500}|
|:-:|
|<div style="width:500px"><b>Caption</b></div>|



# Pipeline description

This example illustrates the analysis of the electron density (ED) calculated for small water clusters, (H2O)x with x = 3, ..., 30.

Quantum chemistry calculations involve `CREST` and `ADF` software, the topological analysis is performed in the `TTK` software.


# Definitions

* for definitions of studied functions, please see [this document](definitions.md)


# The description of the current pipeline (gosia,17/07)

## Molecular systems, data:
CHECK THIS:
- water molecule and water clusters, (H2O)$_x$ for size x=1-30; in total, we consider 30 different systems; in data, we refer to them as Wx;
- each water cluster has many energetic minima; i.e., for each x, we have N$_x$ minima = N$_x$ different structures ("equilibrium geometries"); in data, this is denoted as **state**;
- for each of these states, we consider its normal modes, which represent directions and frequencies of molecular vibrations; 
  the rule counting the normal modes that applies here is $3N_{at} - 6$, where N$_{at}$ is the number of atoms; hence here, for a cluster (H2O)$_x$ that has 3x atoms, there are $3*(3x)-6 = 9x-6$ possible directions, in which we can "distort" the equilibrium structure; in data, this is denoted as **mode**;
- along each of $9x-6$ normal modes of each of N$_x$ minima of (H2O)$_x$, we generate 10 (an arbitrary value) structures by distorting the equilibrium structure in $+\vec{v}$ and $-\vec{v}$ direction, where $\vec{v}$ represents a normal mode vector; by doing this, we arrive at 11 geometries in total (10 distorted + 1 equilibrium); in data, this is denoted as **geom**;
- for each "geom", we calculated two scalar fields: "RHO" (electron density) and "BNP" (bare nuclear potential); the generated vti files contain both fields; we use the grids adapted to the system (i.e., the number of grid points will vary), but we maintain consistent spacing of grid points (here=0.1) and the border around molecule (here=2.0) in each case,
- Notes above also show that we deal with huge number of files; the size of vti file depends on a particular geom (for W6, it seems to be max. 100MB);
- to demonstrate the workflow and the idea, we then selected a few clusters (this example: W6), a few "states" for each, and a few "geoms"; selection criteria are discussed below

## Working examples - selection criteria:
  - Among many possible structural descriptors to classify the structures of water clusters, we considered the ones discussed in https://doi.org/10.1063/5.0009933, in particular:
      - "rings": Trimers, Tetramers, Pentamers, Hexamers; the rings are determined for "projected graphs" of water clusters, in which each water molecule is a node and each hydrogen bond is an edge; see Fig.2 in this paper;
      - our first selection criterion ("sc1"): look for cases, in which the molecular motion causes the number of Hexamers to change; see Fig. 3 in this paper

### Example: W6:
- Number of states, modes, geometries:
  - initial #states (from wdbase) = 80; after the quantum chemistry refinement: #state=54
  - each structure has $9*6-6 = 48$ normal modes, #mode=48; for each mode we generated 10 distorted geometries from an equilibrium structure, #geom=11
  - this gives $54*48*11$ distinct geometries;
  - after applying "sc1", we have just a few cases to consider; a video example of `W6_state_50_mode_20`:

![type:video](./videos/W6_state_50_mode_20.mp4)

- This data is available at https://zenodo.org/records/12779079


# Selection of molecular systems and dataset description (older pipeline)

All datasets used in this example can be downloaded from [Google Disc](https://drive.google.com/drive/u/2/folders/1P1xhseed2snQC7HzYXxu5aY2XLeglGsQ).

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

The quantum chemistry protocol involves the following steps:


## Calculation of scalar functions for the topological data analysis

TODO later

## Topological Data Analysis

TODO later


