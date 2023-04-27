# Exploring the topology of the molecular electrostatic potential in simple molecules

# Pipeline description

This example illustrates the calculation of the molecular electrostatic potential (MESP) of a few simple molecules in the `DIRAC` software, followed by (2) its subsequent topological analysis in the `TTK` software.

## Purpose, questions, tests

* for definitions of MESP please see [this document](link-TODO)

* what we explore here:

  * the anisotropy of the gradient paths of MESP arising from its minima; explored in [this paper]()

* waiting for:

  * ['better' (averaged) partitioning of the molecular domain due to selected topological features of a scalar function](WIP-TODO)
 

* Our test systems:
  
  * H2O (water molecule):
  
    * mol file: [h2o.csv](link)
    * real-space quantum chemistry data in VTI format: [filename](link)
    * `paraview --state=pvsm/C8H8_MESP/MespExploration.pvsm`
  
  * CO:
  
    * mol file: [h2o.csv](link)
    * real-space quantum chemistry data in VTI format: [filename](link)
    * `paraview --state=pvsm/C8H8_MESP/MespExploration.pvsm`
  
  
  * C3H6:
  
    * mol file: [h2o.csv](link)
    * real-space quantum chemistry data in VTI format: [filename](link)
    * `paraview --state=pvsm/C8H8_MESP/MespExploration.pvsm`
  
  
  * C2H6O (oxirane) 
  
    * mol file: [h2o.csv](link)
    * real-space quantum chemistry data in VTI format: [filename](link)
    * `paraview --state=pvsm/C8H8_MESP/MespExploration.pvsm`
  
  
  * C8H8 (cubane):
  
    * mol file: [h2o.csv](link)
    * real-space quantum chemistry data in VTI format: [filename](link)
    * `paraview --state=pvsm/C8H8_MESP/MespExploration.pvsm`

