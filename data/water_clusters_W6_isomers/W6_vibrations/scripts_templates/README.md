# Workflow description

0. prepare scripts:

```
cd ../
cp scripts_templates/main.py .
# adapt main.py
python main.py
```

1. geometry optimization:

  ```
  ./prep_geomopt.sh
  ./run_all_geomopt.sh
  ```

* results are in `geometry_optimization` directory
* optimized geometries are copied to `coordinates/optimized*`

2. real-space calculations on optimized equilibrium structures:

  * if the purpose is to get the grid dimensions, then do fast evaluation and stop:
    ```
    ./prep_rs_eval.sh
    ./run_all_rs_eval.sh
    ```
    * results should be in `explorations_rs_grid_eval` directory


3. real-space calculations on "distorted" structures:

  * first, generate new molecular structures - distort the equilibrium structure along the normal modes;

    On HPC, do this in an interactive environment with paraview activated

    ```
    ./prep_traj.sh
    ```

    you should now have prepared `explorations_rs_trajectories` directory with coordinates; so now - lets prepare jobs for all these files:

  * then, prepare real-space calculations:
    ```
    ./prep_rs_calcs_trajectories.sh
    ```

    * to copy the generated geometries to the `coordinates` directory, run:

    ```
    ./maintanance.sh
    ```

    this is useful to add all coordinates to git and view them locally

    * and run (remember that it should not be done within an interactive session; best to open a new terminal window):

    ```
    ./run_all_rs_trajectories.sh
    ```

4. prepare vti:

  ```
  sbatch run_make_water_clusters_hpc_trajectories.sh
  ```

  This should produce a `sharing_data/helper.txt` file and `*.vti` files in working directories.

4. share

  ```
  ./prep_for_sharing_trajectories.sh
  ```

  This should produce a `sharing_data/*gz` file that can be transfered or shared.

