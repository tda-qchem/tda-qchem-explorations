# Exploring correlations between the electron density, the molecular electrostatic potential, and the bare nuclear potential in simple molecules


# Pipeline description

This example applies the TDA tools for the bivariate analysis of selected molecular descriptors, including the molecular electrostatic potential (MESP), the bare nuclear potential (BNP), the electron density (ED), the reduced density gradient (RDG) and the electron density laplacian (L(ED)) of a few simple molecules.

Data is generated in the `DIRAC` software, the topological analysis is performed in the `TTK` software.



## Purpose, questions, tests

### Definitions:

  * for definitions of MESP, ED, BNP, RDG, L(ED), please see [this document](definitions.md)

  * bivariate functions we explore here:

    * BNP ($V_{nuc}$) and ED ($\rho$)


#### Our test systems:

  * H2O-H2O (water dimer):
  
    * [CSV file with molecular geometry](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/h2o-h2o/geom.csv)
    * real-space quantum chemistry data in VTI format:
      * ED: [density.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/h2o-h2o/dirac/dc_b3lyp_dyallav3z/super/density.128.vti)
      * BNP: [espn.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/h2o-h2o/dirac/dc_b3lyp_dyallav3z/super/espn.128.vti)
    * first explorations: go to the root directory of [this repository](https://github.com/tda-qchem/tda-qchem-explorations) and enter the following command:

      ``` bash
      paraview --state=pvsm/bivariate_ED_MESP_BNP/h2o-h2o_espn_density.pvsm
      ```

   
  * C2H6O (oxirane) 
  
    * [CSV file with molecular geometry](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/oxirane/geom.csv)
    * real-space quantum chemistry data in VTI format:
      * ED: [density.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/oxirane/dirac/dc_b3lyp_dyallav3z/super/density.128.vti)
      * BNP: [espn.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/oxirane/dirac/dc_b3lyp_dyallav3z/super/espn.128.vti)
    * first explorations: go to the root directory of [this repository](https://github.com/tda-qchem/tda-qchem-explorations) and enter the following command:

      ``` bash
      paraview --state=pvsm/bivariate_ED_MESP_BNP/oxirane_espn_density.pvsm
      ```


### Motivation for these explorations:

  * here we run simple tests to understand how we can/should build bivariate analysis protocols for more complex functions and systems:
    * [WIP: exploring the transfer of relativistic effects in halogen-bonded complexes](relativistic-xbs.md)
    * if possible, automatize the workflow and run it on databases, [WIP - exploring $\sigma$-hole interactions](sigma-hole-interactions-database.md))

  * joint analysis of BNP and ED:
    * reassessing homeomorphism between BNP and ED
      * examples we look at: (1) H2O-H2O and (2) oxirane: according to [this work](https://onlinelibrary.wiley.com/doi/full/10.1002/qua.22215), BNP and ED are homeomorphic in (1) but not in (2)


  * joint analysis of MESP and ED:

    * typical analysis of MESP involves plotting MESP on the selected isosurface of ED (typically, $\rho=0.001$) with contrasting colors corresponding to negative and positive MESP areas; this is used to identify the sites on the molecular surface rich/poor in electron density (respectively)

    * examples we look at: WIP



  
