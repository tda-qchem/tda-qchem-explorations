# Exploring the topology of the molecular electrostatic potential in simple molecules

# Pipeline description

This example illustrates the calculation of the molecular electrostatic potential (MESP) of a few simple molecules in the `DIRAC` software, followed by (2) its subsequent topological analysis in the `TTK` software.

## Purpose, questions, tests

MESP represented as a scalar field, here denoted as $V(\vec{r})$

* is calculated as:

  $$V(\vec{r})$$
 
* its negative gradient has a physical interpretation

  $$V(\vec{r})$$
 

A few interesting issues related to MESP analysis are brought up in the literature; here we take a look at some of them using the tools of TDA:

* the gradient paths arising  


 

Our test systems:

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

