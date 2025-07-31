# Description of hydrogen bonds in formamide dimer

![fig:overview_h2o_h2o](screenshots/formamide_dimer_bonds/formamide_dimer_cover.jpg){width=250} | ![fig:overview_](screenshots/formamide_dimer_bonds/formamide_dimer_cover.jpg){width=250} 
:---:|:---:
|<div style="width:500px"><b>An automatic approach based on Topological Data Analysis extracts the structure and the bonding patterns in formamide dimer .......</b></div>|


# Chemical context

Formamide dimer is an example of hydrogen-bonded systems, in which the substantial contribution to the hydrogen bond (HB) is due to *orbital interactions*.
We explore what can be learned from the analysis of its electron density (ED) and the electron localization function (ELF). We confront it with the "deformation density" plots for the total electron density and the density of the selected orbitals.
Specifically, we are interested in the description of charge transfer and polarization effects that are significant mechanisms for the hydrogen bond in this dimer.


# Pipeline description

TODO: adapt to ED, ESP,...
This example illustrates the analysis of the electron density of the water dimer, which aims to describe and discern covalent bonds (O-H) and non-covalent interactions (O---H). First, the electron density (ED) is computed with the `DIRAC` software given the input atom configuration, followed by the generation of the VTI file and a subsequent topological analysis in the `TTK` software.

The first step, which involves quantum chemistry calculations, is to compute the ED scalar field and export it on a 3D grid.

The second step translates data exported from DIRAC in TXT to the VTI format favored by the TTK code. Simultaneously, it applies the resampling filter ("ResampleToImage") without changing the number of grid points or bounds.

The final step involves analyzing the ED scalar field in the `TTK` software.

The analysis starts with extracting all critical point pairs and one-dimensional separatrices of the Morse-Smale complex.
In the next step, the features of chemical significance are selected, including maxima, 2-saddles, and a subset of separatrices that connect 2-saddles to maxima and do not touch the domain's boundary. 
The intermolecular hydrogen bond can be easily isolated: the corresponding $2$-saddle is located outside the isosurface of ED, indicating a much lower density. Thus, saddle-maximum separatrices attached to $2$-saddles with a low density (typically, below $0.1$) are identified as non-covalent bonds (in red, right figure).
The strength of bonds can be evaluated by the topological persistence of the critical point pair involving the $2$-saddle.
Therefore, this analysis can be further refined, in particular by characterizing the importance of the atoms and the strength of the bonds.
The figure above (right plot) also introduces a specific molecular representation: the density of each atom (i.e., its value at the maximum) is visualized with the radius and the color of the corresponding sphere, while covalent and non-covalent bonds are marked with curves of different colors.
No persistence-driven topological simplification was applied to the electron density field at the input of the topological analysis pipeline. 


The essential `TTK` filters employed in this analysis: `MorseSmaleComplex`.

For more details on this analysis, please see the publication XXXXX. All data files generated in this analysis are on [zenodo](XXXXXXXXXXX). All links are [at the bottom of this page](#resources-and-additional-information).


## Quantum chemistry calculations

### Setup



The molecular structure of water dimer in its gas-phase equilibrium geometry was downloaded from [S22 database](http://www.begdb.org/index.php?action=oneMolecule&state=show&id=82) and used in calculations without reoptimization.

ED was calculated analytically in the development version of the `DIRAC` software (commit hash `4fc3ae6`) with the Dirac-Coulomb Hamiltonian, the B3LYP exchange-correlation functional, and the all-electron aug-cc-pVTZ basis set applied to all atoms. The density was exported on the cube grid of 256 points in each Cartesian direction using the default visualization options in `DIRAC`.


### `DIRAC` inputs

* Molecular geometry of water dimer in XYZ format (in Angstrom): [2H2O.xyz](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/H2OH2O_ED_bonds/geom.xyz)
* Input for a wave function optimization: [scf.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/H2OH2O_ED_bonds/dirac/dc_b3lyp_def2tzvp/inputs/scf.inp) <<---RESTART!!
* Input for calculations of the ED scalar field: [ed.inp]()

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
inp_vis=ed.inp
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




