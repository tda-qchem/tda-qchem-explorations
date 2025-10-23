#!/bin/bash

preamble

share_dir_parent=$here/sharing_data

calc_dir=$exec_rs

for m in W6_drop1 W6_bifdrop
do
  share_dir=$share_dir_parent/$m
  mkdir -p $share_dir
  helper_file=$share_dir/helper.txt
  echo "FILE,StructName,GeomID,Coord1,Coord2,Coord3,Energy" >>$helper_file

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
          ns=$tmp'/'$hh'/'$f'/'$b
 
          jobname=rho_bnp
          jobname_shared=rho
          wrkdir=$calc_dir/$n/gridspacing$gridspacing/$jobname
          data_sharing_dirname=data/$ns/gridspacing$gridspacing/$jobname_shared
          analysis_dir=$wrkdir/analysis
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
            echo $data_sharing_dirname/start_data.vti,${m},${strucID},${nx},${ny},${nz},${energy} >>$helper_file
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
    done
  done
done

