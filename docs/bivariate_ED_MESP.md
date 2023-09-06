# Exploring correlations between the electron density and the molecular electrostatic potential.


# Pipeline description

This example applies the TDA tools for the bivariate analysis of selected molecular descriptors, including the molecular electrostatic potential (MESP) and the electron density (ED) of a few simple molecules.

Data is generated in the `DIRAC` software, the topological analysis is performed in the `TTK` software.



## Purpose, questions, tests

### Definitions:

  * for definitions of studied functions, please see [this document](definitions.md)

### Our test systems:

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

   
  * C4H4 (tetrahedrane)
  
    * [CSV file with molecular geometry](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/tetrahedrane/geom.csv)
    * real-space quantum chemistry data in VTI format:
      * ED: [density.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/tetrahedrane/dirac/dc_b3lyp_dyallav3z/super/density.128.vti)
      * BNP: [espn.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/tetrahedrane/dirac/dc_b3lyp_dyallav3z/super/espn.128.vti)
    * first explorations: go to the root directory of [this repository](https://github.com/tda-qchem/tda-qchem-explorations) and enter the following command:

      ``` bash
      paraview --state=pvsm/bivariate_ED_MESP_BNP/tetrahedrane_espn_density.pvsm
      ```


### Motivation for these explorations:

The purpose of these explorations is to apply the TDA tools for the joint analysis of MESP and ED functions, and to assess whether they can help to identify the range of ED isovalues, at which MESP exhibits interesting features.
 
Typical analysis of MESP involves plotting MESP on the selected isosurface of ED (typically, $\rho=0.001$) with contrasting colors corresponding to negative and positive MESP areas. 
This is then used to identify the sites on the molecular surface rich/poor in electron density (respectively).
The problem is that the 0.001 isosurface of ED may not be an optimal heuristic for MESP analysis.



  
