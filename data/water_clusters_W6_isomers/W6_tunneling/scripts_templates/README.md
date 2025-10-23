# Workflow description

* prepare scripts, do real-space calculations

```
cd ../
cp scripts_templates/main.py .
# adapt scripts
python main.py
./prep_rs.sh
./run_all.sh
```

* prepare vti files

```
sbatch run_make_water_clusters_hpc_trajectories.sh
```


* prepare data for sharing:

```
./prep_for_sharing_trajectories.sh
```

This should produce a `sharing_data/*gz` file that can be transfered or shared.


