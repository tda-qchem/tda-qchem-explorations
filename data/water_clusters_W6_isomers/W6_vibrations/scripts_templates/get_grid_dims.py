#!/bin/env python
  
import os
import sys
from glob import glob
from pathlib import Path

fout=sys.argv[1]

with open(fout, 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if " GRID" in line:
            dims = lines[i+2].strip()
            lx = lines[i+3].strip().split()[3]
            ly = lines[i+4].strip().split()[3]
            lz = lines[i+5].strip().split()[3]
            dx = float(lx)/float(dims.split()[0])
            dy = float(ly)/float(dims.split()[1])
            dz = float(lz)/float(dims.split()[2])
            break
if dims is None:
    print('ERROR: no dims for fout ', fout)
else:
    print(dims,lx,ly,lz,dx,dy,dz)
