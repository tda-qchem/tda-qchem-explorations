# Vortices in the magnetically-induced current density in LiH molecule studied through the lens of the Omega function

| ![Omega_bz.png](screenshots/LiH_MICD/repImageGray.png){width=300} |
|:--:|
| An automatic approach based on Topological Data Analysis extracts axial (blue) and toroidal (green) vortices in magnetically-induced current density as specific sub-sets of the separatrices (gray curves) of the Morse-Smale complex of the Omega index. |


# Pipeline description

This example illustrates the calculation of the magnetically-induced current density (MICD) tensor in LiH molecule in the DIRAC software, followed by the calculation of the Omega index with the QCTEN script and its subsequent topological analysis in the TTK software.

The first step involving quantum chemistry calculations aims to export the MICD tensor and its gradient on a regular 3D grid. The setup chosen for these calculations involves the Dirac-Coulomb Hamiltonian, the Density Functional Theory method with the B3LYP functional, the basis set of triple-zeta quality (def-TZVP), the London atomic orbitals and the simple magnetic balance scheme for the generation of a small component set in the presence of a magnetic perturbation. The magnetic field perturbation is applied perpendicularly to the Li-H bond ("Bz"). The cube grid has 128 points in each Cartesian direction and is built with a 4 a.u. of additional space around the molecule (default DIRAC setup).

The purpose of the second step is a pointwise derivation of a scalar function from these tensor fields. In this case, the studied scalar field represent the so-called Omega index, which is used as an indicator of vortices in the first-order current density field. This step also involves translating data exported from DIRAC in CSV format to the VTI format favored by the TTK code. At the same time, it applies the resampling filter ("ResampleToImage") without changing the number of grid points or grid bounds.

The final step involves analyzing the topologically-simplified Omega scalar field in the TTK software. The calculation of its Morse-Smale complex allows to extract the axial vortex as a separatrix connecting a maximum to 2-saddles on the grid boundaries. The calculation of persistent 1-cycle in the super-level sets of Omega allows to extract the toroidal vortex. 

Details of this work can be found in the relevant publication [on arXiv](https://arxiv.org/abs/2212.08690).


## Quantum chemistry calculations

### Inputs and run scripts

<!--- * Molecular geometry of LiH molecule in CSV format (in atomic units): [LiH.csv](../data/LiH_MICD/LiH.csv) --->
* Molecular geometry of LiH molecule in CSV format (in atomic units): [LiH.csv](../data/LiH_MICD/LiH.csv) --->
* Molecular geometry of LiH molecule in CSV format (in atomic units): [LiH.csv](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/LiH_MICD/LiH.csv)
    * This is the experimental geometry from [NIST database](https://cccbdb.nist.gov/exp2x.asp?casno=7580678&charge=0#NISTdiatomic and https://www.nist.gov/pml/diatomic-spectral-database).
* Input(s) for a wave function optimization: [scf.inp](LINK.csv)
* Input(s) for calculations of the magnetic-field response (uses NMR shielding calculations): : [rsp.inp](LINK.csv)
* Run script: [run](run.sh)

### Outputs

* XXX in XXX format

### Execution

* This paragraph assumes that the DIRAC's `pam` script is available in `$PATH` (see prerequisites - TODO, write a separate section)
* Wave function optimization and response calculations:

```
mol=lih.xyz
inp_scf=scf.inp
inp_rsp=rsp.inp
pam --inp=$inp_scf --mol=$mol --outcmo
pam --inp=$inp_rsp --mol=$mol --incmo --get="DFCOEF=DFCOEF.smb TBMO PAMXVC"
```

* Calculations and export of real-space densities:

```
mol=lih.xyz
inp_vis=jbx.inp
pam --inp=$inp_vis --mol=$mol --put="DFCOEF.smb TBMO PAMXVC" --get="plot.3d.vector=jbx.txt"
```

* Tips:
    * For the adaptation of this commands to the HPC environment, check [this page](todo).
    * For the full pipeline automatic execution, check [this page](todo).


### Further description


## Calculation of scalar functions for the topological data analysis

### Inputs
### Outputs
### Run script

## Topological Data Analysis


### Inputs

* Molecular geometry of LiH molecule in CSV format (in atomic units): [LiH.csv](https://github.com/tda-qchem/tda-qchem-explorations/blob/main/data/LiH_MICD/LiH.csv)

* MICD-related data in VTI format:

    * Omega function derived from the magnetically-induced current density vector corresponding to the perturbation of the magnetic field applied perpendicularly to the Li-H bond: [start_data_omega_bz.vti](https://github.com/tda-qchem/tda-qchem-explorations/blob/main/data/LiH_MICD/vti/start_data_omega_bz.vti); data description:
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






