# Exploring correlations between different molecular descriptors: electron density (ED) and electrostatic potential (ESP) in H2O molecule



# Pipeline description

This example illustrates (1) the calculation of the molecular electrostatic potential (MESP), the bare nuclear potential (BNP), the electron density (ED), the reduced density gradient (RDG) and the electron density laplacian (L(ED)) in the H2O molecule in the `DIRAC` software, followed by (2) the subsequent topological analysis in the `TTK` software.


The first step involving quantum chemistry calculations aims to compute the aforementioned scalar functions and their gradient and export them on a 3D grid.

We then form bivariate scalar functions from several pairs of the selected molecular functions, (i) MESP and ED, (ii) BNP and ED, (iii) ED and RDG, (iv) ED and L(ED). 

## Quantum chemistry calculations

### Setup



## Topological Data Analysis

### Inputs

* The molecular geometry of the molecule in CSV format (in atomic units) is available in the [h2o.csv](link) file.

* Real-space quantum chemistry data in VTI format:

    * `start_data_ed.vti` file with ED data: 
    * `start_data_rdg.vti` file with RDG data: 
    * `start_data_led.vti` file with L(ED) data: 
    * `start_data_mesp.vti` file with MESP data: 
    * `start_data_bnp.vti` file with BNP data: 
    * `start_data_mesp_el.vti` file with the data corresponding to the electronic contribution to MESP
    * `start_data_all.vti` file with the data corresponding to all considered functions



### ParaView


* current tests and first conclusions


* Past explorations - Julien's analysis:

```
paraview --state=pvsm/H2O_ED_ESP/fiberSurfaceExploration.pvsm
```

  * data description:
    * *ed* - corresponds to the electron density of H2O molecule
    * *esp* - corresponds to the electrostatic potential of H2O molecule

  * typical analysis protocol in chemistry:
    * plot the *ed* isosurface for an isovalue 0.001 and color it by *esp*






