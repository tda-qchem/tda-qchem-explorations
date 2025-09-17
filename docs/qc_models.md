# Descriptions of models

## Components of the quantum chemistry (QC) model

* Hamiltonians:

    * `DC`: relativistic four-component Dirac--Coulomb Hamiltonian (as implemented in the `DIRAC` software).
    * `ZORA`: relativistic two-component Hamiltonian (as implemented in the `AMS` software), with (`so-ZORA`) and without (`sc-ZORA`) spin-orbit coupling.

* Methods:

    * DFT: Density Functional Theory (with the popular exchange--correlation functionals).
    * DFTB: Density-Functional Tight-Binding methods (GFNn-xTB with n = 0-2).
    * Additional dispersion corrections of Grimme were applied in some cases.

* Basis sets

    * All calculations were done with all-electron uncontracted basis sets.
    * Gaussian-type orbitals are modeled with Dunning sets (`aug-cc-pVXZ`, with `X = D, T, Q`) and Dyall sets (`dyall.cvXz` with `X = 2, 3, 4`)
    * Slater-type orbitals are modeled with sets used in the `AMS` software: `TZP`, `TZ2P`, `QZ4P`.

## Data models

* All real-space data generated in quantum chemistry calculations for subsequent analysis is exported on rectilinear grids. 

## Comments

The main goal for all examples published on this website is educative and demonstrational. Therefore, the choice of the quantum chemistry models was primarily guided by their ability to provide reasonable results relatively quickly for various molecular systems using the selected software. As such, the choice may not always be optimal or "the best" for a specific application.

We mostly used relativistic Hamiltonians, the DFT methods, and all-electron uncontracted basis sets in the presented examples.
By using relativistic Hamiltonians, even for modeling systems with light atoms, we opted for the consistent description of all elements in the periodic table. Then, the DFT methods are, in many cases, cost-effective alternatives to more accurate wave-function-based approaches. In many applications, all-electron relativistic models can be a reliable reference for other theoretical approaches and are indispensable for comparing with experimental results. Many examples could still be reproduced with more modest models by other QC software. On the other hand, more demanding examples, such as the ones involving calculations on weakly bound molecular systems, require wave-function-based methods or DFT functionals crafted for a particular application (to approach chemical accuracy). We comment on these choices in the corresponding publications.



