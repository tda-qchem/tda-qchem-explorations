#!/bin/env python

import os,sys
import shutil
from pathlib import Path

#---------------------------------------------------------------------#
#
# global setup: adapt this part
#
# Note: this is an example, adapt this for each case separately


preamble=[
"project_name='W6_geoms_selected_litgeoms_refined'",
"mol='W6'",
"ham=('nonrel')",
"fun=('PBE0')",
"bas=('TZ2P')",
"gridspacing=0.05",
"Ntest=11",
"here=`pwd`",
"geom_dir=$here/'coordinates'",
"exec_geomopt=$here/'geometry_optimization'",
"exec_rs_0=$here/'explorations_rs_0'",
"exec_rs_grid_eval=$here/'explorations_rs_grid_eval'",
"exec_rs_traj=$here/'explorations_rs_trajectories'",
"exec_rs_traj_scaled=$here/'explorations_rs_trajectories_scaled'",
"src_dir=$here/'scripts_templates'",
"cluster_name='ares'",
]

# make sure these variables are the same as in Bash preamble above:
project_name='W6_geoms_selected_litgeoms_refined'
cluster_name='ares'
here=os.getcwd()
src_dir=here+'/scripts_templates'
#---------------------------------------------------------------------#


#---------------------------------------------------------------------#
# Normally, there should be no need to change this part:
#

# copy this data to all Bash scripts
for p in Path(src_dir).glob("*.sh"):
    new_p=Path(here, p.name).resolve()
    shutil.copy(p, new_p)
    with open(p, 'r') as f:
        with open(new_p, 'w') as g:
            lines = f.readlines()
            for line in lines:
                if 'preamble' in line: 
                    for x in preamble:
                        g.write('{}\n'.format(x))
                    if p.name.startswith('rsync'):
                        g.write('cluster_name={}\n'.format(cluster_name))
                else:
                    g.write(line)

#---------------------------------------------------------------------#

