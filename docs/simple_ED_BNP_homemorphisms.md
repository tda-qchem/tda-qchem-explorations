# Exploring correlations between the electron density and the bare nuclear potential in simple molecules


| ![figure.png](screenshots/EXAMPLE/figure.png) {width=500}|
|:-:|
|<div style="width:500px"><b>Caption</b></div>|


# Pipeline description

This example demonstrates the analysis of the homeomorphism between two molecular descriptors, ED (electron density) and BNP (bare nuclear potential), calculated for a few selected simple molecular systems.

Data is generated in the `DIRAC` software, the topological analysis is performed in the `TTK` software.


# Definitions

* for definitions of studied functions, please see [this document](definitions.md)


# Selection of molecular systems and dataset description

## H2O-H2O (water dimer) - TO REVIEW:

  * [CSV file with molecular geometry](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/h2o-h2o/geom.csv)
  * real-space quantum chemistry data in VTI format:
    * ED: [density.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/h2o-h2o/dirac/dc_b3lyp_dyallav3z/super/density.128.vti)
    * BNP: [espn.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/h2o-h2o/dirac/dc_b3lyp_dyallav3z/super/espn.128.vti)
  * first explorations: go to the root directory of [this repository](https://github.com/tda-qchem/tda-qchem-explorations) and enter the following command:

    ``` bash
    paraview --state=pvsm/bivariate_ED_MESP_BNP/h2o-h2o_espn_density.pvsm
    ```

 
## C2H6O (oxirane) 

  * [CSV file with molecular geometry](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/oxirane/geom.csv)
  * real-space quantum chemistry data in VTI format:
    * ED: [density.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/oxirane/dirac/dc_b3lyp_dyallav3z/super/density.128.vti)
    * BNP: [espn.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/oxirane/dirac/dc_b3lyp_dyallav3z/super/espn.128.vti)
  * first explorations: go to the root directory of [this repository](https://github.com/tda-qchem/tda-qchem-explorations) and enter the following command:

    ``` bash
    paraview --state=pvsm/bivariate_ED_MESP_BNP/oxirane_espn_density.pvsm
    ```

 
## C4H4 (tetrahedrane)

  * [CSV file with molecular geometry](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/tetrahedrane/geom.csv)
  * real-space quantum chemistry data in VTI format:
    * ED: [density.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/tetrahedrane/dirac/dc_b3lyp_dyallav3z/super/density.128.vti)
    * BNP: [espn.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/tetrahedrane/dirac/dc_b3lyp_dyallav3z/super/espn.128.vti)
  * first explorations: go to the root directory of [this repository](https://github.com/tda-qchem/tda-qchem-explorations) and enter the following command:

    ``` bash
    paraview --state=pvsm/bivariate_ED_MESP_BNP/tetrahedrane_espn_density.pvsm
    ```


# Commentary

The purpose of these explorations is to reasses the homeomorphism between BNP and ED function for the (1) H2O-H2O, (2) oxirane, and (3) tetrahedrane molecular systems.
According to [Popelier .....](https://onlinelibrary.wiley.com/doi/full/10.1002/qua.22215), BNP and ED are homeomorphic in system (1) but not in molecules (2) and (3).

As indicated in the cited work, the lack of homeomorphism can be attributed to different reasons

Our analyses show that the ....

We revisit this issue on an example of water clusters in XXXX.








  
