# The magnetically-induced current density in C6H6 molecule

![TODO-FIG](link)


## Pipeline description


## Inputs

* [Molecular geometry of LiH molecule in CSV format (in atomic units)](data/C6H6_MICD/C6H6.csv)

* MICD-related data in VTI format:

  * [Full MICD tensor](todo)
    * data description:
      * *bz_jy* - corresponds to the y-component of the current density vector (*j*) induced by the magnetic field (*b*) applied perpendicularly to the Li-H bond (*z*); etc.

  * [Omega function derived from the magnetically-induced current density vector corresponding to the perturbation of the magnetic field applied perpendicularly to the ring of C atoms](data/C6H6_MICD/vti/start_data_omega_bz.vti)
    * data description:
      * *omega_bz* - corresponds to Omega function calculated for the magnetic field (*b*) applied in z-direction;
      * *bz_wz* - corresponds to the z-component of the curl of the current density vector (*j*) induced by the magnetic field (*b*) applied in z-direction; it is a zz-component of the vorticity tensor.

## Outputs

