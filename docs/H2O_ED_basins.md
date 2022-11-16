# title

<video width="320" height="240" controls>
  <source src="videos/H2O_ED_basins/rotation128.ogv" type="video/mp4">
</video>


| ![figure.png](screenshots/EXAMPLE/figure.png) |
|:--:|
| Caption|


# Pipeline description

This example illustrates the challenges related to the segmentation of a domain of a scalar function into basins of uniform gradient flow from the Morse-Smale complex, in particular:
* proposing a segmentation which respects molecular symmetry and diminishes the the triangulation bias of the algorithms generating simplicial complexes;
* getting a reliable predictions of values integrated over identified basins
 
In this example, we use the electron density (ED) of H2O molecule as a test scalar field.

Currently, we address these challenges by the rotational averaging of basins; this is a work in progress and detailed notes are [here](https://github.com/tda-qchem/tda-segmentation-rotational-averaging-paper/blob/main/notes.md).


## Quantum chemistry calculations

### Inputs and run scripts

* Molecular geometry of H2O molecule in XYZ format (in Angstrom): [mol.xyz](molfile.xyz)
    * Molecular geometry from [Jensen et. al., Journal of Molecular Spectroscopy, 168 (2), 271, 1994](http://www.sciencedirect.com/science/article/pii/S002228528471277X)
* Input for a wave function optimization: [scf.inp](inpfile.csv)
* Input for calculations of the electron density on a cube grid: [ed.inp](inpfile.csv)
* Run script: [run](run.sh)

### Outputs

* XXX in XXX format

### Execution

### Further description


## Topological Data Analysis

### Inputs

* Molecular geometry of H2O molecule in CSV format (in atomic units): [mol.csv](molfile.csv)

* Real-space data in VTI format:

    * Electron density scalar field: [start_data_all.vti](../data/vti/start_data_all.vti); data description:
        * *rho* - electron density of H2O molecule

### Outputs

### ParaView

* state files from Julien:

```
cd data/H2O_ED_basins/pvsm
paraview --state=rotations.pvsm
```

### Python script

### Further description




