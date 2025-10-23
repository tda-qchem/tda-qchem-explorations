#!/bin/bash
  
preamble

calc_dir=$exec_rs_grid_eval

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

        jobname=grid_eval
        wrkdir=$calc_dir/$n/gridspacing$gridspacing/$jobname
        cd $wrkdir
 
        chmod u+x run_$jobname.sh
        sbatch run_$jobname.sh
        echo `pwd`
      done
    done
  done
done
