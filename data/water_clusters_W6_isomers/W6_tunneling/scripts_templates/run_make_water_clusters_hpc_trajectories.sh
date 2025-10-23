#!/bin/bash
#SBATCH -J paraview
#SBATCH -N 1
#SBATCH --ntasks-per-node=8
#SBATCH --mem-per-cpu=5GB
#SBATCH --time=72:00:00 
#SBATCH -A plgqchemtda-cpu
#SBATCH -p plgrid
#SBATCH --output="output.out"
#SBATCH --error="error.err"

srun /bin/hostname
module load paraview/5.11.1-foss-2021b-mpi

./make_water_clusters_hpc_trajectories.sh

cd $SLURM_SUBMIT_DIR
