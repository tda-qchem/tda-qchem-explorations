# Exploring correlations between the electron density, the molecular electrostatic potential, and the bare nuclear potential in simple molecules


# Pipeline description

This example applies the TDA tools for the bivariate analysis of selected molecular descriptors, including the molecular electrostatic potential (MESP), the bare nuclear potential (BNP), the electron density (ED), the reduced density gradient (RDG) and the electron density laplacian (L(ED)) of a few simple molecules.

Data is generated in the `DIRAC` software, the topological analysis is performed in the `TTK` software.



## Purpose, questions, tests

* Definitions:

  * for definitions of MESP, ED, BNP, RDG, L(ED), please see [this document](link-TODO)

  * bivariate functions we explore here:

    * MESP ($V$) and ED ($\rho$): $f(V, \rho)$
    * BNP ($V_{nuc}$) and ED ($\rho$): $f(V_{nuc}, \rho)$
    * ED ($\rho$) and RDG ($s$): $f(\rho, s)$
    * ED ($\rho$) and L(ED) ($\nabla \rho$): $f(\rho, \nabla \rho)$
    * MESP ($V$) and L(ED) ($\nabla \rho$): $f(V, \nabla \rho)$

* Analysis, questions:

  * explorations of MESP and ED, $f(V, \rho)$:

    * typical analysis of MESP involves: plotting MESP on the selected isosurface of ED (typically, $\rho=0.001$) with contrasting colors corresponding to negative and positive MESP areas; this is used to identify the sites on the molecular surface rich/poor in electron density (respectively); here - we investigate an alternative path to do so

    * example 1: water dimer, H2O-H2O 
      * `paraview --state=pvsm/H2OH2O_MESP/fiberSurfaceExploration.pvsm`
    
  * explorations of BNP and ED:


* Our test systems:

  * H2O (water molecule):
  
    * mol file: [h2o.csv](link)
    * real-space quantum chemistry data in VTI format:
      * MESP data: [filename](link)
      * BNP data: [filename](link)
      * ED data: [filename](link)
    * state files:
      * `paraview --state=pvsm/C8H8_MESP/fiberSurfaceExploration.pvsm`



