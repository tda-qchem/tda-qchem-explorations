#!/bin/bash
  
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

        wrkdir_parent=$calc_dir/$n/gridspacing$gridspacing/normal_modes_tracking

        jobname=rho_bnp
        coordir=$wrkdir_parent/generated_structures/summary


        for mode in $coordir/*
        do
          cd $mode
          mode_base=$(basename ${mode})
          for coor in coordinates/*.xyz
          do
            tmp=$(basename ${coor})
            coor_mol=${tmp%.*}

            wrkdir=$wrkdir_parent/calculations/$jobname/$mode_base/$coor_mol
            cd $wrkdir

            chmod u+x run_$jobname.sh
            sbatch run_$jobname.sh
            echo `pwd`

          done
        done
      done
    done
  done
done
