#!/bin/bash

preamble

calc_dir=$exec_geomopt

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

        unr="False"
        ncl="False"
        if [ "$hh" == "spinorbitZORA" ]; then
          unr="True"
          ncl="True"
        fi

        wrkdir=$calc_dir/$n
        jobname=geomopt
        data_dir=$wrkdir/$jobname

        mkdir -p $wrkdir
        cp $mf                                        $wrkdir/
        if [ -f $wrkdir/geomopt0/molecule_optimized_0.xyz  ]; then
          cp $wrkdir/geomopt0/molecule_optimized_0.xyz  $wrkdir/
        fi
        cp $src_dir/pyadf/$jobname.pyadf              $wrkdir/
        cp $src_dir/pyadf/run_$jobname.sh             $wrkdir/

        sed -i "s@DATADIR_THIS@$data_dir@g" $wrkdir/$jobname.pyadf
        sed -i "s@DATADIR_THIS@$data_dir@g" $wrkdir/run_$jobname.sh
        sed -i "s@MOLFILENAME_THIS@$tmp@g"  $wrkdir/$jobname.pyadf
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
        sed -i "s@GRIDSPACING_THIS@$gridspacing@g"  $wrkdir/$jobname.pyadf

      done
    done
  done
done
