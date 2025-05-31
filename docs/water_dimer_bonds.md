# Description of covalent and hydrogen bonds in water dimer

![fig:water_dimer_bonds_cover](screenshots/water_dimer_bonds/water_dimer_bonds_cover.jpg){width=250} | ![fig:water_dimer_bonds_cover](screenshots/water_dimer_bonds/water_dimer_bonds_cover.jpg){width=250} 
:---:|:---:
|<div style="width:500px"><b>An automatic approach based on Topological Data Analysis extracts the structure and the bonding patterns in water dimer as specific critical points (left plot: maxima and 2-saddles marked as dark-green and light-green points) and specific sub-sets of separatrices (right plot: red and blue curves represent low-persistence and high-persistence 1-separatrices between maxima and 2-saddles) of the Morse-Smale complex of the electron density scalar field (gosia - copied from the book).</b></div>|


# Chemical context

Water dimer is an archetypal example of hydrogen-bonded (HB) systems, in which the non-covalent interaction is dominated by the *electrostatic contribution*.
The electron density (ED), its derivatives and their functions (such as Lambda2), and the molecular electrostatic potential (ESP) are some of the best-suited molecular descriptors to explore how such interaction manifests in real space.

Moreover, it is a system exhibiting covalent (O-H) and inter-molecular non-covalent (O---H) interactions between the same types of atoms, in which the hydrogen atoms have three different "roles" (marked as "a", "d", and "f" in the figure below XXXX, denoting the HB acceptor, the HB donor and the free center, respectively).

The primary goal of this example is to illustrate the TDA of the electron density of the water dimer to describe and discern covalent bonds (O-H) and non-covalent interactions (O---H).
A more in-depth analysis of HBs is then followed with the illustration of the joint analysis of ED and Lambda2, and ED and ESP. The latter is more thouroughly discussed in a separate tutorial (LINK). 


# Pipeline description

First, the selected descriptors, ED, Lambda2, and ESP, are computed (analytically) with the `DIRAC` software given the input atom configuration. 
These functions and exported on a 3D grid as HDF5 files.

The second step translates this exported data to the VTI format suitable for the TTK code. Simultaneously, it applies the resampling filter ("ResampleToImage") without changing the number of grid points or bounds.

The final step involves analysis in the `TTK` software.

The analysis starts with extracting all critical point pairs and one-dimensional separatrices of the Morse-Smale complex for the ED field.
In the next step, the features of chemical significance are selected, including maxima, 2-saddles, and a subset of separatrices that connect 2-saddles to maxima and do not touch the domain's boundary. 
The intermolecular hydrogen bond can be easily isolated: the corresponding $2$-saddle is located outside the isosurface of ED, indicating a much lower density. Thus, saddle-maximum separatrices attached to $2$-saddles with a low density (typically, below $0.1$) are identified as non-covalent bonds (in red, right figure).
The strength of bonds can be evaluated by the topological persistence of the critical point pair involving the $2$-saddle.
Therefore, this analysis can be further refined, in particular by characterizing the importance of the atoms and the strength of the bonds.
The figure above (right plot) also introduces a specific molecular representation: the density of each atom (i.e., its value at the maximum) is visualized with the radius and the color of the corresponding sphere, while covalent and non-covalent bonds are marked with curves of different colors.
No persistence-driven topological simplification was applied to the electron density field at the input of the topological analysis pipeline. 


The essential `TTK` filters employed in this analysis: `MorseSmaleComplex`.

For more details on this analysis, please see the publication XXXXX. 
All data files generated in this analysis are on [zenodo](XXXXXXXXXXX). 
All links are [at the bottom of this page](#resources-and-additional-information).


To complement the characterization of HBs, we further visualize the Lambda2 scalar field.

Then, we look for further insight from the ESP scalar field, using the typical aanalysis approach, which is to plot ESP on the selected isosurface of ED (typically, $\rho=0.001$) with contrasting colors corresponding to negative and positive ESP areas. This is then used to identify the sites on the molecular surface rich/poor in electron density (respectively).
The choice of the 0.001 isovalue for ED isosurface is arbitrary (and generally employed in chemistry), but suffices to XXXX.
We further discuss such joint analysis in [this example](bivariate_ED_MESP.md).



## Quantum chemistry calculations

### Setup

The molecular structure of water dimer from [XXXX et.al. XXX](wwwDOI-LINK) (optimized) is used in all calculations without reoptimization.

ED was calculated analytically in the development version of the `DIRAC` software (commit hash `XXXX`) with the Levy-Leblond Hamiltonian, the B3LYP exchange-correlation functional, and the all-electron aug-cc-pVTZ basis set applied to all atoms. The density was exported on the cube grid generated for this molecular system, assuming the 0.05 a.u. grid resolution and the 2.0 a.u. margin (see `DIRAC` manual for the description of visualization options).

### `DIRAC` inputs

* Molecular geometry of water dimer in XYZ format (in Angstrom): [2H2O.xyz](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/H2OH2O_ED_bonds/geom.xyz)
* Input for a wave function optimization: [scf.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/H2OH2O_ED_bonds/dirac/dc_b3lyp_def2tzvp/inputs/scf.inp) <<---RESTART!!
* Input for calculations of the scalar fields: [vis.inp]()

### `DIRAC` outputs

* Files with exported elements of the ED scalar field and and its gradient on a grid in TXT format; these are also available on [zenodo](XXXXX)
* `DIRAC` text output files, available in [the repository](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/dirac/dc_b3lyp_def2tzvp/outputs) and on [zenodo](https://zenodo.org/record/7446735#.Y8BlkNKE4XU).


### Execution

* Below, we assume that the `pam` script of `DIRAC` is available in `$PATH`.

* Step 1. Wave function optimization:

```
mol=2H2O.xyz
inp_scf=scf.inp
pam --inp=$inp_scf --mol=$mol --outcmo
```

* Step 2. Calculations and export of real-space densities,

```
mol=2H2O.xyz
inp_vis=vis.inp
pam --inp=$inp_vis --mol=$mol --put="DFCOEF.smb=DFCOEF TBMO PAMXVC" --get="plot.3d.vector=$vis.txt"
```


## Topological Data Analysis

### Inputs

* The molecular geometry of water dimer in CSV format (in atomic units) is available in the [2H2O.csv](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/LiH.csv) file.

* ED-related data in VTI format:

    * `start_data_ed.vti` file in [the repository](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/vti/start_data_omega_bz.vti) and on [zenodo](https://zenodo.org/record/7446735#.Y8E2dtKZNhF); data description:
        * `ED` - corresponds to the electron density of water dimer


### Outputs

* The `Paraview` state files and all other files enabling the reproduction of the above screenshot and all images attached to the companion publication are in [the repository](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/pvsm).


### ParaView

To reproduce the images and to explore the TDA pipeline, go to the root directory of [this repository](https://github.com/tda-qchem/tda-qchem-explorations) and enter the following command:

``` bash
paraview --state=pvsm/H2OH2O_ED_bonds.pvsm
```

## Resources and additional information

* [Prerequisites](https://tda-qchem.github.io/tda-qchem-examples/)
* [DIRAC](http://www.diracprogram.org/)
* [TTK](https://topology-tool-kit.github.io/)
* [qcten](TODO)

* The calculations and export of the electron density are also discusssed in [the official DIRAC tutorial](XXXX).




