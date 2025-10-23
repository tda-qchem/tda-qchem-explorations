#!/bin/bash

project_name='W6_geoms_selected_litgeoms_refined'
mol='W6'
ham=('nonrel')
fun=('PBE0')
bas=('TZ2P')
gridspacing=0.05
Ntest=11
here=`pwd`
geom_dir=$here/'coordinates'
exec_geomopt=$here/'geometry_optimization'
exec_rs_0=$here/'explorations_rs_0'
exec_rs_grid_eval=$here/'explorations_rs_grid_eval'
exec_rs_traj=$here/'explorations_rs_trajectories'
exec_rs_traj_scaled=$here/'explorations_rs_trajectories_scaled'
src_dir=$here/'scripts_templates'
cluster_name='ares'

#
# copy optimized geometries
#
for mf in $geom_dir/*.xyz
do
  tmp=$(basename $mf)
  m=${tmp%.*}
  for h in "${ham[@]}"
  do
    for f in "${fun[@]}"
    do
      for b in "${bas[@]}"
      do
        hh=$(echo $h | tr -d ' ')
        n=$m'/'$hh'/'$f'/'$b

        wrkdir=$exec_geomopt/$n
        jobname=geomopt
        data_dir=$wrkdir/$jobname

        fout=$wrkdir/$jobname/alloutput*out
        geom_dir_opt=$geom_dir/optimized_${hh}_${f}_${b}/$m
        mkdir -p $geom_dir_opt
        cp $data_dir/molecule_optimized.xyz  $geom_dir_opt/$m.xyz
        cp $data_dir/freqs.txt  $geom_dir_opt/
        cp $data_dir/modes.txt  $geom_dir_opt/
        energy=`python $src_dir/get_energy_from_out.py $fout`
        echo $data_dir > $geom_dir_opt/README.md
        echo $energy >>  $geom_dir_opt/README.md

      done
    done
  done
done

#
# copy geometries along the trajectories
#
for mf in $geom_dir/*.xyz
do
  tmp=$(basename $mf)
  m=${tmp%.*}
  for h in "${ham[@]}"
  do
    for f in "${fun[@]}"
    do
      for b in "${bas[@]}"
      do
        hh=$(echo $h | tr -d ' ')
        n=$m'/'$hh'/'$f'/'$b

        coordir=$exec_rs_traj/$n/gridspacing$gridspacing/normal_modes_tracking/generated_structures/summary
        coordir_saved=$geom_dir/trajectories_along_normal_modes/${m}_${hh}_${f}_${b}
        echo $coordir $coordir_saved
        mkdir -p $coordir_saved
        cp -r $coordir/* $coordir_saved

        echo "COPIED FROM: " $coordir >> $coordir_saved/README.md

      done
    done
  done
done

#
# copy geometries along the trajectories: scaled
#
#for mf in $geom_dir/*.xyz
#for mf in $geom_dir/*prism_mp2.xyz
#do
#  tmp=$(basename $mf)
#  m=${tmp%.*}
#  for h in "${ham[@]}"
#  do
#    for f in "${fun[@]}"
#    do
#      for b in "${bas[@]}"
#      do
#        hh=$(echo $h | tr -d ' ')
#        n=$m'/'$hh'/'$f'/'$b
#
#        coordir=$exec_rs_traj_scaled/$n/gridspacing$gridspacing/normal_modes_tracking/generated_structures/summary
#        coordir_saved=$geom_dir/trajectories_along_normal_modes_scaled/${m}_${hh}_${f}_${b}
#        echo $coordir $coordir_saved
#        mkdir -p $coordir_saved
#        cp -r $coordir/* $coordir_saved
#
#        echo "COPIED FROM: " $coordir >> $coordir_saved/README.md
#
#      done
#    done
#  done
#done



