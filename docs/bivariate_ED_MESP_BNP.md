# Exploring correlations between the electron density, the molecular electrostatic potential, and the bare nuclear potential in simple molecules


# Pipeline description

This example applies the TDA tools for the bivariate analysis of selected molecular descriptors, including the molecular electrostatic potential (MESP), the bare nuclear potential (BNP), the electron density (ED), the reduced density gradient (RDG) and the electron density laplacian (L(ED)) of a few simple molecules.

Data is generated in the `DIRAC` software, the topological analysis is performed in the `TTK` software.



## Purpose, questions, tests

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





### Definitions:

  * for definitions of MESP, ED, BNP, RDG, L(ED), please see [this document](link-TODO)

  * bivariate functions we explore here:

    * MESP ($V$) and ED ($\rho$): $f(V, \rho)$
    * BNP ($V_{nuc}$) and ED ($\rho$): $f(V_{nuc}, \rho)$
    * ED ($\rho$) and RDG ($s$): $f(\rho, s)$
    * ED ($\rho$) and L(ED) ($\nabla \rho$): $f(\rho, \nabla \rho)$
    * MESP ($V$) and L(ED) ($\nabla \rho$): $f(V, \nabla \rho)$


### Our test systems:

  * H2O-H2O (water dimer):
  
    * mol file: [h2o-h2o.csv](../data/h2o-h2o/geom.csv)
    * real-space quantum chemistry data in VTI format:
      * ED: [density.128.vti](../data/h2o-h2o/vti/dirac/dc_b3lyp_dyallav3z/super/density_visgrid_cube_128/density.128.vti)
      * BNP: [espn.128.vti](../data/h2o-h2o/vti/dirac/dc_b3lyp_dyallav3z/super/espn_visgrid_cube_128/espn.128.vti)
    * `paraview --state=pvsm/bivariate_ED_MESP_BNP/H2OH2O_espn_density.pvsm`
   
  * C2H6O (oxirane) 
  
    * mol file: [oxirane.csv](../data/oxirane/geom.csv)
    * real-space quantum chemistry data in VTI format:
      * ED: [density.128.vti](../data/oxirane/vti/dirac/dc_b3lyp_dyallav3z/super/density_visgrid_cube_128/density.128.vti)
      * BNP: [espn.128.vti](../data/oxirane/vti/dirac/dc_b3lyp_dyallav3z/super/espn_visgrid_cube_128/espn.128.vti)
    * `paraview --state=pvsm/bivariate_ED_MESP_BNP/oxirane_espn_density.pvsm`
  
