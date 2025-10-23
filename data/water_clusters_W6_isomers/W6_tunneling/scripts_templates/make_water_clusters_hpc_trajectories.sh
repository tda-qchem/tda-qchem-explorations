#!/bin/bash

# remember to do this first:
# srun   -p plgrid -t 72:00:00 -N 1 --ntasks-per-node=8 -A plgqcembed-cpu   --pty /bin/bash -l
# srun   -p plgrid-now -t 12:00:00 -N 1 --ntasks-per-node=8 -A plgqcembed-cpu   --pty /bin/bash -l
# module load paraview/5.11.1-foss-2021b-mpi

preamble

calc_dir=$exec_rs
tmpl_dir=$src_dir/qcten_scripts_templates/templates


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
          analysis_dir=$wrkdir/analysis
          mkdir -p $analysis_dir
  
          for f in $wrkdir/*.csv
          do
            datafile=$(realpath $f)
            fileformat=${f##*.}
            if [ -f $f ] 
            then
              cp $datafile $analysis_dir
            fi
          done
          fout=$wrkdir/alloutput*out
          if [ -f $fout ] 
          then
  
            cd $analysis_dir
  
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
            energy=`python $src_dir/get_energy_from_out.py $fout`
  
            # electron density only:
            cp $tmpl_dir/on_hpc/prep_denscsv.py  .
            cp $tmpl_dir/prep_denscsv.inp .
            # note we swap nx with nz!
            sed -i "s@nx@$nz@" prep_denscsv.inp
            sed -i "s@ny@$ny@" prep_denscsv.inp
            sed -i "s@nz@$nx@" prep_denscsv.inp
            python prep_denscsv.py
  
          fi
          cd $here
        done
      done
    done
  done
done

