# Description of hydrogen bonds in formamide dimer

<div class="grid" markdown>

![fig:overview_formamide_dimer](screenshots/formamide_dimer_bonds/formamide_dimer_cover.jpg)

![fig:overview_formamide_dimer_diff](screenshots/formamide_dimer_bonds/formamide_dimer_cover.jpg)

</div>

<div style="font-size: 75%;"><b><i>
WRITEME: An automatic approach based on Topological Data Analysis extracts the structure and the bonding patterns in water dimer as specific critical points (left plot: maxima and 2-saddles marked as dark-green and light-green points) and specific sub-sets of separatrices (right plot: red and blue curves represent low-persistence and high-persistence 1-separatrices between maxima and 2-saddles) of the Morse-Smale complex of the electron density scalar field of this molecular system. In the right plot, the colors and radii of spheres corresponding to atoms are based on topological information. 
</i></b></div>

---


# Chemical context

Formamide dimer is an example of hydrogen-bonded systems, in which the substantial contribution to the hydrogen bond (HB) is due to *orbital interactions*.
Here, we analyze the electron density (ED, $\rho(\vec{r})$) and its derivatives, such as the reduced density gradient (RDG, $s(\vec{r})$) and the sign of the Laplacian of the ED (L2(ED), $sign(\lambda_2)\rho(\vec{r})$), of this dimer and two monomers. We confront it with the QTAIM picture and the so-called *"deformation density"* plots. In addition to the total electron density, we also explore the densities of the selected molecular orbitals.
Specifically, we are interested in the description of charge transfer and polarization effects that are significant mechanisms for the hydrogen bond in this dimer.

Formamide dimer has two HBs.... GOSIA-TODO:description+figure

![fig:formamide_dimer_bonds_geom](screenshots/formamide_dimer_bonds/geom.png){width=50%}


# Pipeline description

All quantum chemistry calculations are done analytically in the `DIRAC` software. Exported scalar fields are then transformed to `VTI` files - one for each molecular system (i.e., the dimer and each monomer) and one for each demonstration (i.e., the total densities and those corresponding to selected molecular orbitals).

WRITEME


## Quantum chemistry calculations

### Setup

The molecular structure of formamide dimer in its gas-phase equilibrium geometry was downloaded from the [S22 database](http://www.begdb.org/index.php?action=oneMolecule&state=show&id=82) and used in calculations without reoptimization. The geometries of monomers are as in the dimer.

All calculations were done analytically, using the development version of the `DIRAC` software (commit hash `XXXX`). The quantum chemistry model was based on the Levy-Leblond Hamiltonian, the B3LYP exchange-correlation functional, and the all-electron aug-cc-pVTZ basis set applied to all atoms. All molecular descriptors studied in this tutorial were exported on the rectilinear grid generated for the dimer, assuming the 0.05 a.u. grid resolution and the 2.0 a.u. margin (see `DIRAC` manual for the description of visualization options). The same grid was used for each monomer.


### `DIRAC` inputs

* Molecular geometries in XYZ format (in Angstrom):
    * of the dimer: [geom.xyz](../data/formamide_dimer/coordinates/geom.xyz)
    * of the first monomer: [geom.xyz](../data/formamide_dimer/coordinates/geom.xyz)
    * of the second monomer: [geom.xyz](../data/formamide_dimer/coordinates/geom.xyz)
* Input for a wave function optimization: 
    * of the dimer: [scf.inp](TODO)
    * of each monomer: [scf.inp](TODO)
* Input for calculations of scalar fields:
    * of the dimer: [vis.inp](TODO)
    * of each monomer: [vis.inp](TODO)

### Calculations

With the `pam` script of `DIRAC` available in `$PATH`, the calculations are done in two steps.
For example, for the dimer:

* Step 1. Wave function optimization:

```
mol=geom.xyz
inp_scf=scf.inp
pam --inp=$inp_scf --mol=$mol --outcmo
```

* Step 2. Calculations and export of real-space densities:

```
mol=geom.xyz
inp_vis=vis.inp
pam --inp=$inp_vis --mol=$mol --incmo --get="ed*.h5 rdg.h5"
```

See `DIRAC` manual for "Resources and additional information".
This procedure should be repeated for each monomer, using dedicated inputs (as listed above).

## Generation of VTI files

We provide a script for reformatting HDF5 files exported from `DIRAC` into one VTI file used by `TTK`: [prep_vti.sh](../python/utils/prep_vti.sh).
It needs an input file, which contains the names of HDF5 files that should be used; this is provided as [prep_vti.inp](../data/formamide_dimer/vti/super/prep_vti.inp) ADAPT

Copy these two files to the directory containing HDF5 files exported from `DIRAC` and execute:

```
./prep_vti.sh 
```

Simultaneously, this applies the resampling filter ("ResampleToImage") without changing the number of grid points or the domain's bounds.
We do this to change the type of input data from a 'point cloud data' to a 'uniform rectilinear grid data', which is optimal for TTK.

The workflow demonstrated here is adapted to data organized into three folders - for the dimer ("supermolecule" in `data/vti/super`) and the two monomers ("subsystems", in `data/vti/sub1` and `data/vti/sub2`).

All VTI files can also be downloaded from [Zenodo](https://zenodo.org/records/17223709).



## Topological Data Analysis

GOSIA/JULIEN-TODO: prepare pvsm and python scripts

To reproduce the images and to explore the TDA pipeline, use the [PVSM](pvsm/formamide_dimer_bonds/ed_rdg_led.pvsm) state file or the [PYTHON](python/formamide_dimer_bonds/ed_rdg_led.py) script:

* create (see sections above) `VTI` files or download the tar and unpack it to the `data/formamide_dimer/vti` directory; the data is organized into three folders - one for the dimer (as [super/start_data_ed_rdg_led.vti](`data/formamide_dimer/vti/super/start_data_ed_rdg_led.vti`)) and two for the two monomers (as [sub1/start_data_ed_rdg_led.vti](`data/formamide_dimer/vti/sub1/start_data_ed_rdg_led.vti`) and [sub2/start_data_ed_rdg_led.vti](`data/formamide_dimer/vti/sub2/start_data_ed_rdg_led.vti`)) 

* go to the root directory of this repository ([here](../)) and enter the following command:

GOSIA-draft 1: working on the scatterplot, f(ED) vs. f(RDG) for the dimer:

```
paraview --state=pvsm/formamide_dimer_bonds/ed_rdg_led.pvsm
```

GOSIA-draft 2: exploring the ED difference, ED(super)-ED(sub1)-ED(sub2):

```
paraview --state=pvsm/formamide_dimer_bonds/ed_difference.pvsm
```

GOSIA-draft 3: comparing ED(super) with f=ED(sub1)+ED(sub2):

```
paraview --state=pvsm/formamide_dimer_bonds/ed_and_edsubsum.pvsm
```



or run the python script (TODO later?):

```
pvpython python/formamide_dimer_bonds/ed_rdg_led.py
```

These scripts also import input atomic coordinates (in a.u.), which are in the [`geom.csv`](`data/formamide_dimer/coordinates/geom.csv`) file.



## Resources and additional information

* [Prerequisites](https://tda-qchem.github.io/tda-qchem-examples/)
* [DIRAC](http://www.diracprogram.org/)
* useful `DIRAC` tutorials:
    * [links](XXXX).
* [TTK](https://topology-tool-kit.github.io/)
* useful `TTK` tutorials:
    * [Molecule1](https://topology-tool-kit.github.io/examples/interactionSites/)
    * [Molecule2](https://topology-tool-kit.github.io/examples/morseMolecule/)
    * [Bivariate analysis](https://topology-tool-kit.github.io/examples/builtInExample2/)
* [qcten](TODO)





