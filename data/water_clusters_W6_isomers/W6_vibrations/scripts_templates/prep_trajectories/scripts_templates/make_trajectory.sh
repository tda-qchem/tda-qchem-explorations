#!/bin/bash

Ntest=NTEST_THIS

rm -f *.sdf

for f in *.xyz
do
  mol=${f%.*}
  obabel -ixyz -osdf $mol.xyz > $mol.sdf
done

out_sdf="trajectory.sdf"
out_xyz="trajectory.xyz"
rm -f $out_sdf $out_xyz

for (( i = 0; i < $Ntest -1; i++ )) 
do
  n="geom_"$i
  cat $n*sdf >>$out_sdf
  cat $n*xyz >>$out_xyz
done

#
# if needed, this can be adapted to reindex nodes from -max,...,max
#
#for (( i = $Ntest -1; i > 0; i-- )) 
#do
#  n="geom_minus_"$i
#  cat $n*sdf >>$out_sdf
#  cat $n*xyz >>$out_xyz
#done
#
#n="geom_0_"
#cat $n*sdf >>$out_sdf
#cat $n*xyz >>$out_xyz
#
#for (( i = 1; i < $Ntest; i++ )) 
#do
#  n="geom_plus_"$i
#  cat $n*sdf >>$out_sdf
#  cat $n*xyz >>$out_xyz
#done
