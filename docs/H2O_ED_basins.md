# title

| ![figure.png](screenshots/EXAMPLE/figure.png) |
|:--:|
| Caption|


# Pipeline description

This example illustrates the challenges related to the segmentation of a domain of a scalar function into basins of uniform gradient flow from the Morse-Smale complex. As an example, we use the electron density of H2O molecule.

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

    * Electron density scalar field: [start_data_XXXX.vti](file.vti); data description:
        * *ed* - electron density

### Outputs

### ParaView

### Python script

### Further description




