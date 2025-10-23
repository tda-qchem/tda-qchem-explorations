#!/bin/bash
  
preamble

calc_dir=$exec_rs

for m in W6_drop1 W6_bifdrop
do
  for mf in $geom_dir/$m"_prep"/*.xyz
  do
    base=${mf##*/}
    tmp=${base%.*}
    IFS='_' read -r -a tmp2 <<< "$tmp"
    strucID="${tmp2[3]}"

    for h in "${ham[@]}"
    do
      for f in "${fun[@]}"
      do
        for b in "${bas[@]}"
        do
          hh=$(echo $h | tr -d ' ')
          n=$m'/'$tmp'/'$hh'/'$f'/'$b
  
          jobname=rho_bnp
          wrkdir=$calc_dir/$n/gridspacing$gridspacing/$jobname
          cd $wrkdir
   
          chmod u+x run_$jobname.sh
          sbatch run_$jobname.sh
          echo `pwd`
        done
      done
    done
  done
done
