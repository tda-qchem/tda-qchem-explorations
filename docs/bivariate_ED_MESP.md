# Exploring correlations between the electron density and the molecular electrostatic potential.


# Pipeline description

This example applies the TDA tools for the bivariate analysis of selected molecular descriptors, including the molecular electrostatic potential (MESP) and the electron density (ED) of a few simple molecules.

Data is generated in the `DIRAC` software, the topological analysis is performed in the `TTK` software.



## Purpose, questions, tests

### Definitions:

  * for definitions of studied functions, please see [this document](definitions.md)

### Our test systems:

  * WIP

### Motivation for these explorations:

The purpose of these explorations is to apply the TDA tools for the joint analysis of MESP and ED functions, and to assess whether they can help to identify the range of ED isovalues, at which MESP exhibits interesting features.
 
Typical analysis of MESP involves plotting MESP on the selected isosurface of ED (typically, $\rho=0.001$) with contrasting colors corresponding to negative and positive MESP areas. 
This is then used to identify the sites on the molecular surface rich/poor in electron density (respectively).
The problem is that the 0.001 isosurface of ED may not be an optimal heuristic for MESP analysis.



  
