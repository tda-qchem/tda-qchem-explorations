# Description

This website collects examples of TDA applications to Quantum Chemistry. It is a scratch repository for generating examples discussed in the TDA-QCHEM book.

Each example includes:

* inputs and run scripts for a relevant quantum chemistry software
* a short description of outputs from quantum chemistry calculations
* screenshots from [TTK](https://topology-tool-kit.github.io/)
* a ParaView state file that allows reproducing the figures
* a short description of outputs and analysis in [TTK](https://topology-tool-kit.github.io/)
* a Python code that allows reproducing the full workflow
* links to quantum chemistry software and [TTK](https://topology-tool-kit.github.io/) documentation

This website also contains:

* A list of molecular descriptors (with the notation and analytical formulas): [link](definitions.md)
* A short description of quantum chemistry and data models used in all calculations: [link](models.md)

How to cite this website: 

* Gosia - TODO: (1) mention it is a companion to our book, (2) add DOI


# Prerequisites

These examples assume a default installation of [DIRAC](http://www.diracprogram.org/), [TTK](https://topology-tool-kit.github.io/) and [qcten](https://github.com/gosiao/qcten).
Selected examples also use [CREST](XXX) and [AMS](xxx) software. Among all these codes, only `AMS` is commercial; however, all quantum chemistry data is also available for download at [this link](xxx).


# Full pipeline automatization

writeme

# List of examples

Summary and work progress: [LINK](XXXX)


## Completed and published

| Name | Screenshot |
|:-:|:-:|
|[The magnetically-induced current density in LiH molecule studied with the Omega function](LiH_MICD/)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|


### Referred to in the book (unpublished)

| Name | Screenshot |
|:-:|:-:|
|[Description of covalent and hydrogen bonds in water dimer](H2OH2O_ED_bonds)|![ExampleImage](screenshots/H2OH2O_ED_bonds/h2o_h2o_bondPersistence.jpg){width=300}|
|[Intramolecular hydrogen bonds in derivatives of 1H-pyrrole](C5H6ON2_ED_bonds)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|
|[Description of simple halogen bonds: At-At $\cdots$ NH3 example](AtAtNH3_ED_RDG_bonds)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|
|[Elusive intramolecular Au $\cdots$ H non-covalent interaction in a small gold complexes](elusiveAuH_ED_RDG_bonds)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|




## WIP (only placeholders in the book)

| Name | Screenshot |
|:-:|:-:|
|[Exploring correlations between the electron density and the bare nuclear potential in a few selected simple molecules](simple_ED_BNP_homemorphisms.md)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|
|[Exploring correlations between the electron density and the bare nuclear potential in a set of water clusters](water_clusters_ED-BNP-homeomorphism.md)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|
|[Exploring correlations between the electron density and the molecular electrostatic potential](bivariate_ED_MESP.md)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|
|[Exploring the topology of the molecular electrostatic potential in simple molecules](MESP_theory)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|


### Calculations in progress:

|[Potential energy surface exploration: description of isomers in a set of water clusters](water_clusters_PES_isomers.md)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|

|[Exploring the transfer of relativistic effects in halogen-bonded complexes](relativistic-xbs)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|
|[Exploring $\sigma$-hole interactions through the topology of the molecular electrostatic potential and the electron density on benchmark data sets](sigma-hole-interactions-database)|![ExampleImage](screenshots/LiH_MICD/repImageGray.jpg)|



### Old files, need review:

[The magnetically-induced current density in C6H6 molecule studied with the Omega function](C6H6_MICD/)
[The magnetically-induced current density in C4H4 molecule studied with the Omega function](C4H4_MICD/)
[Partitioning of a scalar function and integration over basins: electron density of H2O molecule](H2O_ED_basins/)



## List of molecular systems under study




