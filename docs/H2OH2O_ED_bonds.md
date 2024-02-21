# Description of covalent and hydrogen bonds in water dimer

REWORK

 ![fig:overview_h2o_h2o](screenshots/H2OH2O_ED_bonds/h2o_h2o_criticalPoints.jpg){width=300} | 
 ![fig:overview_h2o_h2o](screenshots/H2OH2O_ED_bonds/h2o_h2o_bondPersistence.jpg){width=300}  
|:-:|
|<div style="width:500px"><b>An automatic approach based on Topological Data Analysis extracts the structure and the bonding patterns in water dimer as specific critical points 
(left plot: maxima and 2-saddles marked as dark-green and light-green points) and specific sub-sets of separatrices (right plot: red and blue curves represent low-persistence and high-persistence 1-separatrices between maxima and 2-saddles) of the Morse-Smale complex of the electron density scalar field.</b></div>|


# Pipeline description

This example illustrates the analysis of the electron density of the water dimer aimed at the description and discernment of covalent bonds (O-H) and non-covalent interactions (O---H). First, the electron density (ED) is computed with the `DIRAC` software given the input atom configuration, followed by the generation of the VTI file and a subsequent topological analysis in the `TTK` software.

The first step involving quantum chemistry calculations aims to compute the ED scalar field and export it on a 3D grid.

The purpose of the second step is to translate data exported from `DIRAC` in TXT to the VTI format favored by the `TTK` code. Simultaneously, it applies the resampling filter ("ResampleToImage") without changing the number of grid points or grid bounds.

The final step involves analyzing the ED scalar field in the `TTK` software. 

The analysis starts with extracting all critical point pairs and one-dimensional separatrices of the Morse-Smale complex. 
In the next step, the features of chemical significance are selected, including maxima, 2-saddles, and a subset of separatrices which connect 2-saddles to maxima and do not touch the boundary of the domain. 
The intermolecular hydrogen bond can be easily isolated: the corresponding $2$-saddle is located outside of the isosurface of ED, which indicates that it has a much lower
density. Thus, saddle-maximum separatrices attached to $2$-saddles with a low density (typically, below $0.1$) are identified as non-covalent bonds (in red, right figure).
The strength of bonds can be evaluated by the topological persistence of the critical point pair involving the $2$-saddle.
This analysis can therefore be further refined, in particular by characterizing the importance of the atoms and the strength of the bonds.
One suggestion is demonstrated in the figure above (right plot): the density of each atom is visualized with the radius and the color of the corresponding sphere, while covalent and non-covalent bonds are marked with curves of different colors.
No persistence-driven topological simplification was applied to the electron density field at the input of the topological analysis pipeline. By construction, this field is smooth and exhibits no noise.


The notable `TTK` filter employed in this analysis is the `MorseSmaleComplex`.


For more details on this analysis, please see the publication XXXXX. All data files generated in this analysis are on [zenodo](XXXXXXXXXXX). All links are [at the bottom of this page](#resources-and-additional-information).


-----------


## Quantum chemistry calculations

### Setup

see /media/gosia/Transcend/qchem_visualization_repo_reviewed/explorations/h2o-h2o
see `\cite{seijas.etal_ijms_2023}` - M062X/aug-cc-pVTZ + CP and CCSD(T)/CBS/CBS no CP.


The molecular structure of water dimer in its gas-phase equilibrium geometry was downloaded from [XXX]() and reoptimized with XXX

The ED and its gradient were calculated analytically in the development version of the `DIRAC` software (commit hash `XXXXX`) with the Dirac-Coulomb Hamiltonian, the B3LYP exchange-correlation functional, and the def-TZVP basis set applied for both atoms. London atomic orbitals and the simple magnetic balance scheme were applied in response calculations. The densities were exported on the cube grid of 128 points in each Cartesian direction using the default visualization options in `DIRAC`.



First, we consider the topology of its electron density, modeled with the DFT method using the DC Hamiltonian, B3LYP exchange-correlation functional and the basis set of 3$\zeta$ quality\footnote{The relativistic DC Hamiltonian is not necessary for this molecular system, yet, since in the latter part of the book, we will compare the topologies of H$_2$X-H$_2$O dimers (with X denoting heavy elements of the oxygen family), we opt for the consistent description of all systems in this series. Also, only all-electron four-component models can serve as a reliable reference for other theoretical approaches and and are indispensable for comparison with experimental results. All methods are discussed in~\autoref{sec:descriptors_concepts_bonds}} and exported on a regular 256$^3$-point grid.
~                                                                                                                                                             


### `DIRAC` inputs

* Molecular geometry of LiH molecule in XYZ format (in Angstrom): [2H2O.xyz](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/LiH.xyz)
* Input for a wave function optimization: [scf.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/dirac/dc_b3lyp_def2tzvp/inputs/scf.inp)
* Input for calculations of the ED scalar field: [ed.inp]()
* Input for calculations of the reduced gradient of ED scalar field: [rdg.inp]()

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
        * `ED` - corresponds to Omega function calculated for the magnetic field applied perpendicularly to the Li-H bond ("bz");


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

* Related data: the publication on [arXiv](XXXXXXXX) and its [1-page summary](), data files generated in this analysis on [zenodo](https://zenodo.org/record/7446735#.Y8BlkNKE4XU).

* To fully reproduce the results reported in the publication, please check [this link]().
* To fully reproduce the publication, please check [this link]().



