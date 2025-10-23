#!/bin/bash -l
#SBATCH -J pyadf_getgrid
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
project=rho_bnp
cp $project.pyadf   $data_dir
cp *.xyz            $data_dir/

srun /bin/hostname

module purge
module load miniconda3/23.5.2-0
eval "$(conda shell.bash hook)"

conda activate /net/pr2/projects/plgrid/plggqcembed/devel/tools/conda_environments/pyadf-main-env/env
config='/net/pr2/projects/plgrid/plggqcembed/devel/tools/pyadf-jobrunner-ADF2021.conf'

cd $data_dir
pyadf -c $config  $project.pyadf

cd $SLURM_SUBMIT_DIR
