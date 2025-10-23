#!/bin/env python

import os,sys
import shutil
from pathlib import Path

#---------------------------------------------------------------------#
#
# global setup: adapt this part
#

preamble=[
"project_name='W6_geoms_along_tunneling_pathways'",
"mol='W6'",
"ham=('nonrel')",
"fun=('PBE0')",
"bas=('TZ2P')",
"gridspacing=0.05",
"here=`pwd`",
"geom_dir=$here/'coordinates'",
"exec_rs=$here/'explorations_rs'",
"src_dir=$here/'scripts_templates'",
"cluster_name='ares'",
]

# make sure these variables are the same as in Bash preamble above:
project_name='W6_geoms_along_tunneling_pathways'
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

