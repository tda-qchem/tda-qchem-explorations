#!/bin/bash -l
#SBATCH -J adf_geomopt
#SBATCH -N 1
#SBATCH --ntasks-per-node=8
#SBATCH --mem-per-cpu=5GB
#SBATCH --time=72:00:00 
#SBATCH -A plgqchemtda-cpu
#SBATCH -p plgrid
#SBATCH --output="output.out"
#SBATCH --error="error.err"

export data_dir=DATADIR_THIS
mkdir -p $data_dir

cd $SLURM_SUBMIT_DIR
project=LandscapeRefinement
cp *.adf   $data_dir/

srun /bin/hostname
module purge
module load adf/2023.104

cd $data_dir
$AMSBIN/ams < $project.adf > $project.out

cd $SLURM_SUBMIT_DIR


