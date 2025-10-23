#!/bin/bash

# remember to do this first:
# srun   -p plgrid -t 72:00:00 -N 1 --ntasks-per-node=8 -A plgqcembed-cpu   --pty /bin/bash -l
# srun   -p plgrid-now -t 12:00:00 -N 1 --ntasks-per-node=8 -A plgqcembed-cpu   --pty /bin/bash -l
# module load paraview/5.11.1-foss-2021b-mpi


preamble

calc_dir=$exec_rs_traj
tmpl_dir=$src_dir/qcten_scripts_templates/templates

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
   
        jobname=rho_bnp
        wrkdir_parent=$calc_dir/$n/gridspacing$gridspacing/normal_modes_tracking/calculations/$jobname
        coordir=$calc_dir/$n/gridspacing$gridspacing/normal_modes_tracking/generated_structures/summary

        for mode in $coordir/*
        do
          cd $mode
          mode_base=$(basename ${mode})
          for coor in coordinates/*.xyz
          do
            tmp=$(basename ${coor})
            coor_mol=${tmp%.*}

            wrkdir=$wrkdir_parent/$mode_base/$coor_mol
            analysis_dir=$wrkdir/analysis
            mkdir -p $analysis_dir

            # split file name:
            IFS='_' read -a TMPS <<< "$coor_mol"
            geom_ind="${TMPS[1]}"
            mode_ind="${TMPS[3]}"
            #echo "coor_mol geom_ind mode_ind: " $coor_mol " -- " $geom_ind " -- " $mode_ind
            data_sharing_dirname=data/$n/gridspacing$gridspacing/normal_modes_tracking/calculations/$jobname/mode${mode_ind}/geom_${geom_ind}_mode_${mode_ind}
      
            for f in $wrkdir/*
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

              cp $tmpl_dir/on_hpc/prep_csv.py  .
              cp $tmpl_dir/prep_csv.inp .
              # note we swap nx with nz!
              sed -i "s@nx@$nz@" prep_csv.inp
              sed -i "s@ny@$ny@" prep_csv.inp
              sed -i "s@nz@$nx@" prep_csv.inp
              python prep_csv.py

            fi
          done
          cd $here
        done
      done
    done
  done
done

