#!/bin/bash

# remember to do this first:
# srun   -p plgrid -t 72:00:00 -N 1 --ntasks-per-node=8 -A plgqchemtda-cpu   --pty /bin/bash -l
# module load paraview/5.11.1-foss-2021b-mpi openbabel
 
preamble

calc_dir=$exec_rs_traj

for mf in $geom_dir/*.xyz
do
  tmpg=$(basename $mf)
  m=${tmpg%.*}
  for h in "${ham[@]}"
  do
    for f in "${fun[@]}"
    do
      for b in "${bas[@]}"
      do
        hh=$(echo $h | tr -d ' ')
        n=$m'/'$hh'/'$f'/'$b
        echo $mf $m $n

        optgeomdir=$exec_geomopt/$n/geomopt

        # get grid info based on evaluation done on the equilibrium structure;
        # this may be useful to generate "distorted structures":

        grid_eval_dir=$exec_rs_grid_eval/$n/gridspacing$gridspacing/grid_eval
        fout=$grid_eval_dir/pyadf*.out
        ndim=`python $src_dir/get_grid_dims.py $fout`
        read -ra arr -d '' <<<"$ndim"
        nx="${arr[0]}"
        ny="${arr[1]}"
        nz="${arr[2]}"
        lx="${arr[3]}"
        ly="${arr[4]}"
        lz="${arr[5]}"
        dx="${arr[6]}"
        dy="${arr[7]}"
        dz="${arr[8]}"

        wrkdir_parent=$calc_dir/$n/gridspacing$gridspacing/normal_modes_tracking

        jobname=generated_structures
        wrkdir=$wrkdir_parent/$jobname
        mkdir -p $wrkdir/coordinates
        mkdir -p $wrkdir/summary

        # generate structures along all normal modes
        cp $optgeomdir/molecule_optimized.xyz       $wrkdir/
        cp $optgeomdir/freqs.txt                    $wrkdir/
        cp $optgeomdir/modes.txt                    $wrkdir/
        cp $optgeomdir/alloutput*out                $wrkdir/geom.out
        
        Nmodes=`wc -l < $wrkdir/freqs.txt`

        cp $src_dir/prep_trajectories/scripts_templates/* $wrkdir/

        sed -i "s@MOLNAME_THIS@$m@g"                $wrkdir/*.sh
        sed -i "s@GRIDSPACING_THIS@$gridspacing@g"  $wrkdir/*.sh
        sed -i "s@NMODES_THIS@$Nmodes@g"            $wrkdir/*.sh
        sed -i "s@NTEST_THIS@$Ntest@g"              $wrkdir/*.sh
        sed -i "s@DX_THIS@$dx@g"                    $wrkdir/*.sh
        sed -i "s@DY_THIS@$dy@g"                    $wrkdir/*.sh
        sed -i "s@DZ_THIS@$dz@g"                    $wrkdir/*.sh

        sed -i "s@MOLNAME_THIS@$m@g"                $wrkdir/*.txt
        sed -i "s@GRIDSPACING_THIS@$gridspacing@g"  $wrkdir/*.txt
        sed -i "s@NTEST_THIS@$Ntest@g"              $wrkdir/*.txt
        sed -i "s@DX_THIS@$dx@g"                    $wrkdir/*.txt
        sed -i "s@DY_THIS@$dy@g"                    $wrkdir/*.txt
        sed -i "s@DZ_THIS@$dz@g"                    $wrkdir/*.txt

        cd $wrkdir

        python generate_distorted_structures_along_normal_mode.py
        # all structures should be in $wrkdir/coordinates directory

        # prepare separate directories for each mode
        # in this workflow, modes numbering starts from 0
        cd $wrkdir/summary

        cp $wrkdir/coordinates/*mode*xyz  .
        for  (( i = 0; i < $Nmodes; i++ ))
        do
          thisdir=mode$i
          mkdir -p $thisdir/coordinates
        
          mv *mode_$i.*                  $thisdir/
          cp $wrkdir/make_trajectory.sh  $thisdir/
        
          cd $thisdir
          chmod u+x make_trajectory.sh
          ./make_trajectory.sh
        
          mv geom*.xyz          coordinates/
          mv geom*.sdf          coordinates/
          rm -f make_trajectory.sh
          cd ../
        done
        cd $here
      done
    done
  done
done
