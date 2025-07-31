# The joint analysis of the electron density and the molecular electrostatic potential.


# Chemical context

This example demonstrates the bivariate analysis of the electron density (ED) and the electrostatic potential (and its components, i.e., ESP, ESPE, ESPN, see [equations](definitions.md)).

There are multiple contexts to these explorations.
First, we demonstrate the analysis of the electron density (ED) and the bare nuclear potential (ESPN) that aims to explore whether there is a homeomorphism between these two fields (the more precise context is discussed in [XXX](link)). We apply this analysis to two molecular systems, water dimer and oxirane molecule, since they are discussed in the literature as examples of 


Then, we show the joint analysis of the electron density (ED) and the electrostatic potential (ESP) 

These two functions are often considered complementary descriptors of chemical information, with the ED well-suited to describe covalent bonds, and RDG for characterization of non-covalent interactions (NCIs).

Precisely, this analysis is done for the logarithms of these two fields (to facilitate handling large differences of ED values in different points in space due to the exponential decay of ED from the atomic center; it does not affect the results of the analysis).

The technical details of this analysis and its practical realization are also available [as the official TTK tutorial](https://topology-tool-kit.github.io/examples/builtInExample2/)


WIP

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



# OLD: Exploring correlations between different molecular descriptors: electron density (ED) and electrostatic potential (ESP) in H2O and H2O-H2O dimer

1. vti file:

```
 wget -O data/H2O_and_H2OH2O_ED_ESP/vti/start_data_all.vti  https://drive.google.com/file/d/1Nglav8vKkLUeiqOjjkWiZKVLGEfo_5ET/view?usp=share_link 
```


2. 

```
paraview --state=pvsm/H2O_and_H2OH2O_ED_ESP/test.pvsm
```

  * data description:
    * *rho* - corresponds to the electron density
    * *esp* - corresponds to the electrostatic potential


  
