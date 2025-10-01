# title


<div class="grid" markdown>

![fig:REF](screenshots/XXX/XXX.jpg)

![fig:REF](screenshots/XXX/XXX.jpg)

</div>

<div style="font-size: 75%;"><b><i>
An automatic approach based on Topological Data Analysis ....
</i></b></div>

---

# Chemical context

This example illustrates ...

# Pipeline description

First, we compute the selected functions - ....
This is an input to the `TTK` software, in which we perform the topological analysis. 

This VTI file can be downloaded from [Zenodo](https://zenodo.org/records/XXXX); 
alternatively, we provide the details for the QC calculations and outline the procedure to generate the VTI file in a separate section below.

For  more details on this analysis, please see ...

The final step involves analyzing the selected scalar fields in the `TTK` software. 

## Topological analysis of the XXX


# Technical details

## Quantum chemistry calculations

### Setup

The molecular structure of XXXXXXXX from XXXXXXXXX is used in all calculations without reoptimization. 
All molecular descriptors were calculated analytically in the development version of the `DIRAC` software (commit hash `XXXX`) with the Levy-Leblond Hamiltonian, the B3LYP exchange-correlation functional, and the all-electron aug-cc-pVTZ basis set applied to all atoms. All molecular descriptors studied in this tutorial were exported on the rectilinear grid generated for this molecular system, assuming the 0.05 a.u. grid resolution and the 2.0 a.u. margin
(see `DIRAC` manual for the description of visualization options).

### `DIRAC` inputs

* Molecular geometry of XXXX in XYZ format (in Angstrom): [geom.xyz](../data/XXXX/coordinates/geom.xyz)
* Input for the wave function optimization: [scf.inp](../data/XXXXX)
* Input for calculations of scalar fields: [vis.inp](../data/XXXXX)

### Calculations

Assuming the `pam` script of `DIRAC` is present in `$PATH`, the calculations are performed in two steps.

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
pam --inp=$inp_vis --mol=$mol --incmo --get="*.h5"
```

See `DIRAC` manual for "Resources and additional information"


## Generation of VTI files

We provide a script for reformatting HDF5 files exported from `DIRAC` into one VTI file used by `TTK`: [prep_vti.sh](../python/utils/prep_vti.sh).
It needs an input file, which contains the names of HDF5 files that should be used; this is provided as [prep_vti.inp](../data/XXX/vti/prep_vti.inp)

Copy these two files to the directory containing HDF5 files exported from `DIRAC` and execute:

```
./prep_vti.sh 
```

Simultaneously, this applies the resampling filter ("ResampleToImage") without changing the number of grid points or the domain's bounds.
We do this to change the type of input data from a 'point cloud data' to a 'uniform rectilinear grid data', which is optimal for TTK.

This VTI file can also be downloaded from [Zenodo](https://zenodo.org/records/XXX).


## Topological Data Analysis

GOSIA/JULIEN-TODO: prepare pvsm and python scripts

To reproduce the images and to explore the TDA pipeline, use the [PVSM](LINK) state file or the [PYTHON](LINK) script:

* create (see sections above) or download the `VTI` file to the `data/XXXX/vti` directory (as [start_data_ed_rdg_led.vti](LINK))

* go to the root directory of this repository ([here](../)) and enter the following command:

```
paraview --state=pvsm/XXX/XXX.pvsm
```

or run the python script (TODO?):

```
pvpython python/pvsm/XXX/XXX.py
```

These scripts also import input atomic coordinates (in a.u.), which are in the [`geom.csv`](`data/XXX/coordinates/geom.csv`) file.




