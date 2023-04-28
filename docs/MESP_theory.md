# Exploring the topology of the molecular electrostatic potential in simple molecules

# Pipeline description

This example illustrates the calculation of the molecular electrostatic potential (MESP) of a few simple molecules in the `DIRAC` software, followed by (2) its subsequent topological analysis in the `TTK` software.


## Purpose, questions, tests

### Definitions:

  * for definitions of MESP, please see [this document](definitions.md)
  * we also use the electron density (ED), calculated with the same setup and on the same grid


#### Our test systems:

  * H2O-H2O (water dimer):
  
    * [CSV file with molecular geometry](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/h2o-h2o/geom.csv)
    * real-space quantum chemistry data in VTI format:
      * ED: [density.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/h2o-h2o/dirac/dc_b3lyp_dyallav3z/super/density.128.vti)
      * MESP: [espn.128.vti](https://github.com/tda-qchem/tda-qchem-explorations/tree/main/data/h2o-h2o/dirac/dc_b3lyp_dyallav3z/super/esp.128.vti)
    * first explorations: go to the root directory of [this repository](https://github.com/tda-qchem/tda-qchem-explorations) and enter the following command:

      ``` bash
      paraview --state=pvsm/bivariate_ED_MESP_BNP/h2o-h2o_mesp.pvsm
      ```

 
  * H2O (water molecule):
  * CO:
  * C3H6:
  * C2H6O (oxirane) 
  * C8H8 (cubane):


### Motivation for these explorations:

  * we are exploring:

    * the anisotropy of the gradient paths of MESP arising from its minima; explored in [this paper]()
    * the asymptotic formulation of the Poincare-Hopf relation (related literature: []())


* this work is also waiting for:

  * ['better' (averaged) partitioning of the molecular domain due to selected topological features of a scalar function](WIP-TODO)
 

 
