# Descriptions of models

## Components of the quantum chemistry model

* Hamiltonians:

    * `DC`: relativistic four-component Dirac--Coulomb Hamiltonian (as implemented in the `DIRAC` software);
    * `ZORA`: relativistic two-component Hamiltonian (as implemented in the `AMS` software), with (`so-ZORA`) and without (`sc-ZORA`) spin-orbit coupling.

* Methods:

    * DFT: Density Functional Theory with the following exchange--correlation functionals: `B3LYP`, `BP86`;
	* DFTB (Density-Functional Tight-Binding methods), GFNn-xTB (n = 0, 1, 2; extended Tight-Binding methods for geometries, frequencies and NCIs) - variants of the DFT;
    * The dispersion correction of Grimme was applied in some cases, when used in conjunction with calculations in the `AMS` software (mentioned as the `-D` suffix in the DFT functional names).

* Basis sets

    * All calculations were done with all-electron uncontracted basis sets
    * Gaussian-type orbitals are modeled with Dunning sets (`aug-cc-pVXZ`, with `X = D, T, Q`) and Dyall sets (`dyall.cvXz` with `X = 2, 3, 4`)
    * Slater-type orbitals are modeled with sets used in the `AMS` software: `TZP`, `TZ2P`, `QZ4P`.

## Data models

* All real-space data generated in quantum chemistry calculations for a subsequent analysis is exported on rectangular grids. 

## Comments

The main goal for all examples published on this website is educative and demonstrational. Therefore, the choice of the quantum chemistry models was primarily guided by their ability to provide reasonable results relatively quickly for various molecular systems using the selected software. As such, the choice may not always be optimal or "the best" for a specific application. For example, we mostly used relativistic Hamiltonians, the DFT methods, and all-electron uncontracted basis sets.

By using relativistic Hamiltonians, even for modeling systems with light atoms, we opted for the consistent description of all elements in the periodic table. Then, the DFT methods are, in many cases, cost-effective alternatives to more accurate wave-function-based approaches. In numerous applications, all-electron relativistic models can be a reliable reference for other theoretical approaches and are indispensable for comparing with experimental results. However, many examples considered here could be reproduced with more modest choices. On the other hand, more demanding examples, such as the ones involving calculations on weakly bound molecular systems, require wave-function-based methods or DFT functionals crafted for a particular application (for instance to approach chemical accuracy). We comment on these choices in the corresponding publications.


## References


