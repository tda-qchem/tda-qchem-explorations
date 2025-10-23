#!/usr/local/bin/pvpython

import os
import sys
sys.path.insert(0, '/net/people/plgrid/plggosiao/devel/ttkqc/')
import ttkqc.process_input
import ttkqc.ttk.ttk_start as ttk0
import ttkqc.ttk.ttk_cps   as ttkcps
import ttkqc.ttk.ttk_multi as ttkmulti


def read_input(finp):
    args = []
    with open(finp, "r") as f:
        for line in f:
            if line[0] != '#' and line != '\n':
                args.append(line.strip())
        return args

# electron density ony
inp = "prep_denscsv.inp"
args=read_input(inp)
data = ttkqc.process_input.input_data(args)
data.parse_options()
data.print_options()
data.prepare_csvdata_files_for_ttk()

ttk_data = ttk0.ttk_start(data.options, data.ttk_start_data)
ttk_data.from_csv_to_start_data()

