#!/bin/bash
  
preamble

calc_dir=$exec_geomopt

cd $calc_dir

for mol in *
do
  for h in "${ham[@]}"
  do
    for f in "${fun[@]}"
    do
      for b in "${bas[@]}"
      do
        hh=$(echo $h | tr -d ' ')
        n=$calc_dir'/'$mol'/'$hh'/'$f'/'$b
        cd $n
        echo `pwd`
        jobname=geomopt
        chmod u+x run_$jobname.sh
        sbatch run_$jobname.sh
      done
    done
  done
done

cd $here


