# Exploring $\sigma$-hole interactions on a benchmark molecular database


| ![figure.png](screenshots/sigma-hole-interactions-database/figure.png) {width=500}|
|:-:|
|<div style="width:500px"><b>Caption</b></div>|

# Pipeline description

This example applies the TDA tools to study $\sigma$-hole non-covalent interactions in a set of molecular complexes selected from the [SH250x10 dataset](http://www.nciatlas.org/SH250.html), and presented [this paper](https://pubs.rsc.org/en/content/articlelanding/2022/cp/d2cp01600a).

Specifically, we selected 20 systems obtained by the autors by applying clustering analysis; these systems (listed in the first row of Table S4 therein) have indices: 
1.1.01, 1.2.02, 1.2.08, 2.2.02, 2.3.01, 2.3.10, 2.7.01, 3.1.02, 3.3.10, 3.3.15, 3.4.03, 4.1.11, 4.2.05, 5.1.05, 5.1.11, 6.1.11, 6.2.04, 6.2.16, 7.2.01, 7.2.03r.
Additionally, here we only consider these complexes at their equilibrium geometries. 

Our goal for this analysis is (i) to demonstrate the workflow that explores the non-covalent interactions, for which the charge transfer and electron (de)localization are crucial

First, we start with the analysis of the electron density (ED) and its derivatives, including the reduced density gradient (RDG), XXXXX. 
Then, to look into the electron localization, we analyze the ELF, XXXX 
Then, we also analyze the molecular electrostatic potential (MESP) of these complexes.
Finally, we demonstrate which information can be extracted from the bivariate analysis of MESP and ED...

Below, we describe these steps in more detail.

All data is generated in the `DIRAC` software, the topological analysis is performed in the `TTK` software.

For  more details on this analysis, please see XXXX.
All links are [at the bottom of this page](#resources-and-additional-information).


## Quantum chemistry calculations

description of a molecular system and of QM model used in calculations

### Inputs and run scripts

* Molecular geometry of XXX molecule in XYZ format (in Angstrom): [mol.xyz](molfile.xyz)
* Input(s) for a wave function optimization: [inp.inp](inpfile.csv)
* Input(s) for calculations of XXXX: : [inp.inp](inpfile.csv)
* Run script: [run](run.sh)

### Outputs

* XXX in XXX format

### Execution


## Calculation of scalar functions for the topological data analysis

### Inputs
### Outputs
### Run script


## Topological Data Analysis

### Inputs

* Molecular geometry of XXX molecule in CSV format (in atomic units): [mol.csv](molfile.csv)

* Real-space data in VTI format:

    * XXXXX function derived from XXXX: [start_data_XXXX.vti](file.vti); data description:
        * *f1* - description;
        * *f2* - description;
        * ...

### Outputs

### ParaView

### Python script


## Resources and additional information

* [Prerequisites](https://tda-qchem.github.io/tda-qchem-examples/)
* [DIRAC](http://www.diracprogram.org/)
* [TTK](https://topology-tool-kit.github.io/)

* Related data:


