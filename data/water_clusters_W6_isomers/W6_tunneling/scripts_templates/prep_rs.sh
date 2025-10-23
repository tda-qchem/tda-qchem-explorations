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
          echo $base  $tmp $strucID $n
  
          unr="False"
          ncl="False"
          if [ "$hh" == "spinorbitZORA" ]; then
            unr="True"
            ncl="True"
          fi
  
          jobname=rho_bnp
          wrkdir=$calc_dir/$n/gridspacing$gridspacing/$jobname
          data_dir=$wrkdir
          mkdir -p $wrkdir
  
          cp $mf                           $wrkdir/
          cp $src_dir/pyadf/$jobname.pyadf           $wrkdir/$jobname.pyadf
          cp $src_dir/pyadf/run_$jobname.sh          $wrkdir/run_$jobname.sh
  
          sed -i "s@DATADIR_THIS@$data_dir@g" $wrkdir/$jobname.pyadf
          sed -i "s@DATADIR_THIS@$data_dir@g" $wrkdir/run_$jobname.sh
          sed -i "s@MOLFILENAME_THIS@$mf@g"   $wrkdir/$jobname.pyadf
          sed -i "s@MOLCHARGE_THIS@0@g"       $wrkdir/$jobname.pyadf
          if [ "$h" != "nonrel" ]; then
            sed -i "s@HAMILTONIAN_THIS@$h@g"    $wrkdir/$jobname.pyadf
            sed -i "s@UNRESTRICTED_THIS@$unr@g" $wrkdir/$jobname.pyadf
            sed -i "s@NONCOLLINEAR_THIS@$ncl@g" $wrkdir/$jobname.pyadf
          else
            sed -i "/HAMILTONIAN_THIS/d"    $wrkdir/$jobname.pyadf
            sed -i "/UNRESTRICTED_THIS/d"    $wrkdir/$jobname.pyadf
            sed -i "/NONCOLLINEAR_THIS/d"    $wrkdir/$jobname.pyadf
          fi
          sed -i "s@DFTFUN_THIS@$f@g"         $wrkdir/$jobname.pyadf
          sed -i "s@BASISSET_THIS@$b@g"       $wrkdir/$jobname.pyadf
          sed -i "s@GRIDSPACING_THIS@$gridspacing@g" $wrkdir/$jobname.pyadf
  
        done
      done
    done

  done
done

#done
