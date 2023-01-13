# Vortices in the magnetically-induced current density in LiH molecule studied through the lens of the Omega function

| ![Omega_bz.png](screenshots/LiH_MICD/repImageGray.png){width=300} |
|:--:|
| An automatic approach based on Topological Data Analysis extracts axial (blue) and toroidal (green) vortices in magnetically-induced current density as specific sub-sets of the separatrices (gray curves) of the Morse-Smale complex of the Omega index. |


# Pipeline description

This example illustrates the calculation of the magnetically-induced current density (MICD) tensor in the LiH molecule in the DIRAC software, followed by the calculation of the Omega index with the QCTEN script and its subsequent topological analysis in the TTK software.



The first step involving quantum chemistry calculations aims to compute the MICD tensor and its gradient and export them on a 3D grid. 



The purpose of the second step is a pointwise derivation of a scalar function from these tensor fields. In this case, the studied scalar field represents the so-called Omega index, used as an indicator of vortices in the first-order current density field. This step also involves translating data exported from DIRAC in TXT to the VTI format favored by the TTK code. Simultaneously, it applies the resampling filter ("ResampleToImage") without changing the number of grid points or grid bounds.



The final step involves analyzing the Omega scalar field in the TTK software. It starts with extracting all critical point pairs, determining a persistence threshold for the salient pairs, and using this threshold to simplify the topology of the Omega scalar field. Then, the computation of the Morse-Smale complex of such simplified field results, in particular, in the extraction of its one-dimensional separatrices. A subset of these separatrices connecting 2-saddles and maxima well captures the center lines of vortices. These can then be associated with axial and toroidal vortices in the MICD of the LiH molecule. Notable TTK filters employed in this analysis are the `PersistenceDiagram`, `TopologicalSimplification`, `MorseSmaleComplex`, and `PersistentGenerators`.



Details of this work can be found in the publication [on arXiv](https://arxiv.org/abs/2212.08690). All data files, particularly those that result from the first two steps of the above-described analysis procedure, can be downloaded from [zenodo](https://zenodo.org/record/7446735#.Y8BlkNKE4XU).



## Quantum chemistry calculations

### Setup

The experimental geometry of LiH molecule from the [NIST database](https://cccbdb.nist.gov/exp2x.asp?casno=7580678&charge=0#NISTdiatomic and https://www.nist.gov/pml/diatomic-spectral-database) was used (R(Li-H) = 1.595 Angstrom).

The MICD tensor and its gradient were calculated analytically in the development version of the [DIRAC](http://www.diracprogram.org/) software (commit hash `2330f11`) with the Dirac-Coulomb Hamiltonian, the B3LYP exchange-correlation functional, and the def-TZVP basis set applied for both atoms. London atomic orbitals and the simple magnetic balance scheme were applied in response calculations. The densities were exported on the cube grid of 128 points in each Cartesian direction using the default visualization options in DIRAC.


### DIRAC inputs and run scripts

* Molecular geometry of LiH molecule in CSV format (in atomic units): [LiH.csv](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/LiH.csv)
* Input for a wave function optimization: [scf.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/dirac/dc_b3lyp_def2tzvp/inputs/scf.inp)
* Input for calculations of the magnetic-field response (uses NMR shielding calculations): [prp.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/dirac/dc_b3lyp_def2tzvp/inputs/prp.inp)
* Input for calculations of the components of the MICD tensor, composed of the elements of the current density vector induced by the magnetic field applied in 
    the "x"-direction ([jbx.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/dirac/dc_b3lyp_def2tzvp/inputs/visgrid_cube_128/jbx.inp)), 
    the "y"-direction ([jby.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/dirac/dc_b3lyp_def2tzvp/inputs/visgrid_cube_128/jby.inp)), and 
    the "z"-direction ([jbz.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/dirac/dc_b3lyp_def2tzvp/inputs/visgrid_cube_128/jbz.inp))
* Input for calculations of the components of the gradient of the MICD tensor, composed of the elements of the gradient of the current density vector induced by the magnetic field applied in 
    the "x"-direction ([gradjbx.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/dirac/dc_b3lyp_def2tzvp/inputs/visgrid_cube_128/gradjbx.inp)), 
    the "y"-direction ([gradjby.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/dirac/dc_b3lyp_def2tzvp/inputs/visgrid_cube_128/gradjby.inp)), and 
    the "z"-direction ([gradjbz.inp](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/dirac/dc_b3lyp_def2tzvp/inputs/visgrid_cube_128/gradjbz.inp))

### Outputs

* XXX in XXX format

### Execution

* This paragraph assumes that the DIRAC's `pam` script is available in `$PATH`
* Wave function optimization:

```
mol=lih.xyz
inp_scf=scf.inp
pam --inp=$inp_scf --mol=$mol --outcmo
```

* Response calculations:

```
mol=lih.xyz
inp_rsp=rsp.inp
pam --inp=$inp_rsp --mol=$mol --incmo --get="DFCOEF=DFCOEF.smb TBMO PAMXVC"
```


* Calculations and export of real-space densities, example for the `jbx.inp` file:

```
mol=lih.xyz
vis=jbx
inp_vis=$vis.inp
pam --inp=$inp_vis --mol=$mol --put="DFCOEF.smb TBMO PAMXVC" --get="plot.3d.vector=$vis.txt"
```

## Calculation of scalar functions for the topological data analysis

### Inputs
### Outputs
### Run script


## Topological Data Analysis

### Inputs

* Molecular geometry of LiH molecule in CSV format (in atomic units): [LiH.csv](https://github.com/tda-qchem/tda-qchem-explorations/blob/main/data/LiH_MICD/LiH.csv)

* MICD-related data in VTI format:

    * Omega function derived from the magnetically-induced current density vector corresponding to the perturbation of the magnetic field applied perpendicularly to the Li-H bond: [start_data_omega_bz.vti](https://github.com/tda-qchem/tda-qchem-explorations/blob/tree/data/LiH_MICD/vti/start_data_omega_bz.vti); data description:
        * *omega_bz* - corresponds to Omega function calculated for the magnetic field (*b*) applied perpendicularly to the Li-H bond (*z*);
        * *bz_wz* - corresponds to the z-component of the curl of the current density vector (*j*) induced by the magnetic field (*b*) applied perpendicularly to the Li-H bond (*z*); it is a zz-component of the vorticity tensor.

### Outputs


### ParaView

To reproduce the above screenshot, go to the root directory of [this repository](https://github.com/tda-qchem/tda-qchem-explorations) and enter the following command:
``` bash
paraview --state=pvsm/lih.pvsm
```

### Python script

### Further description






