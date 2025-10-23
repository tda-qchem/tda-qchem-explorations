#!/bin/bash

preamble

calc_dir=$exec_rs_traj
share_dir_parent=$here/sharing_data

for mf in $geom_dir/*.xyz
do
  tmpg=$(basename $mf)
  m=${tmpg%.*}
  s=${m%"_mp2"}

  share_dir=$share_dir_parent/$m
  mkdir -p $share_dir
  helper_file=$share_dir/helper.txt
  echo "FILE,StructName,ModeID,GeomID,Coord1,Coord2,Coord3,Energy" >>$helper_file

  for h in "${ham[@]}"
  do
    for f in "${fun[@]}"
    do
      for b in "${bas[@]}"
      do
        hh=$(echo $h | tr -d ' ')
        n=$m'/'$hh'/'$f'/'$b
   
        jobname=rho_bnp
        # focus on rho only:
        jobname_shared=rho
        wrkdir_parent=$calc_dir/$n/gridspacing$gridspacing/normal_modes_tracking/calculations/$jobname
        coordir=$calc_dir/$n/gridspacing$gridspacing/normal_modes_tracking/generated_structures/summary

        if [ -d $coordir ] 
        then
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

              # split file name:
              IFS='_' read -a TMPS <<< "$coor_mol"
              geom_ind="${TMPS[1]}"
              mode_ind="${TMPS[3]}"
              #echo "coor_mol geom_ind mode_ind: " $coor_mol " -- " $geom_ind " -- " $mode_ind
              data_sharing_dirname=data/$n/gridspacing$gridspacing/normal_modes_tracking/calculations/$jobname_shared/mode${mode_ind}/geom_${geom_ind}_mode_${mode_ind}

              fout=$wrkdir/alloutput*out
              if [ -f $fout ] 
              then

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
                # note: on vti file we swap nx with nz!
                echo $data_sharing_dirname/start_data.vti,${s},${mode_ind},${geom_ind},${nx},${ny},${nz},${energy} >>$helper_file
              fi

              if [ -d $analysis_dir ] 
              then
              
                cd $analysis_dir

                if [ -f start_data.vti ] 
                then
                  share_base=$share_dir/$data_sharing_dirname
                  mkdir -p $share_base
                  cp start_data.vti $share_base/
                fi
                cd $here
              fi
            done
          done
        fi
      done
    done
  done

#TMP  cd $share_dir
#TMP  # adapt the tar name
#TMP  tar -zcvf W6_selected_litgeoms_refined_DFT_$m.tar.gz *
#TMP  cd $here
done


