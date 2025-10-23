#!/bin/env python

import os
import sys
from glob import glob
from pathlib import Path

fout=sys.argv[1]

with open(fout, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "Energy (hartree)" in line:
            energy=line.strip().split()[-1]
if energy is None:
    print('ERROR: no energy for fout ', fout)
else:
    print(energy)

