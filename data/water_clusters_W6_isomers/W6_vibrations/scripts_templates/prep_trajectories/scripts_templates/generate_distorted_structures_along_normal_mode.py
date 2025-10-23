#!/bin/env python
import re
import sys
import numpy as np
from pathlib import Path
from collections import OrderedDict
from pprint import pprint

#last rev. gosia, 10/02/2025
scale_freq=False
if len(sys.argv) >1:
    sf=sys.argv[1]
    scale_freq=True

constants = {}
constants["angstrom_to_bohr"] = 1.8897259886
constants["bohr_to_angstrom"] = 0.529177249
constants["amu_to_kg"]        = 1.660539040E-27   # kg
constants["planck_constant"]  = 6.62607015E-34    # m2 kg / s
constants["speed_of_light"]   = 2.99792458E+8     # m/s
constants["Avogadro_number"]  = 6.022140857E+23   # 1/mol


def read_global_setup(fh):
    setup={}
    with open(fh, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] != "#": 
                l=line.strip().split("=")
                setup[l[0]]=l[1]
    for k,v in setup.items():
        print(k,v)
    return setup


def estimate_turning_point(nu, Mred):
    """
    Q = (Mred * nu )^{-1/2} * (h/c)^{1/2} * (1/(2pi))
      * Mred = reduced mass of this mode [input in amu -> here, recalculated to kg]
      * nu = wave number from ADF output of this mode [input in cm-1 -> here, recalculated to m-1]
      * h = Planck's constant [kg*m^2/s]
      * c = speed of light [m/s]
      * on output: Q [Angstrom]
    """

    factor = np.sqrt(constants["planck_constant"]/constants["speed_of_light"]) * (1/(2*np.pi))
    Q = factor / np.sqrt(Mred * constants["amu_to_kg"] * 100*nu) * 1.0E+10 

    return Q


def reduced_mass(atom_masses, vib_coords):
    """
    calculate the reduced mass as
      Mred = L^T * M * L

      where L = the matrix with the eigenvectors of the force constant matrix ("vib_coord")
            M = the matrix of atomic masses ("atom_masses")

    on input:
      * atom_masses = M, units = u, type = np.ndarray(3*Nat) of floats
      * vib_coords  = L, units = Bohr/Angstrom, type=np.ndarray(3*Nat,Nvib) of floats - eigenvectors of mass-reduced Hessian printed in ADF output as "Displacements"
    on output:
      * reduced_mass - , units = u, type = np.ndarray(3*Nvib) of floats
    """

    # first, translate vib_coords to Angstrom and reshape them to np.array(3*Nat, Nvib):
    # note: from comparison with ADF2023, it seems that the displacements are in Angstrom already
    #fac = lambda t: constants["bohr_to_angstrom"] * t
    fac = lambda t: 1.0 * t
    vibcoords = np.array([fac(x) for x in vib_coords]).T.flatten()
    # calculate Mred:
    Mred = vibcoords.T.dot(np.diag(np.repeat(atom_masses,3))).dot(vibcoords)
    return Mred

def round_up_to_odd(f):
    f = int(np.ceil(f))
    return f + 1 if f % 2 == 0 else f

def generate_structures(k_ind, k, num_frames, results_path, vibrations, atoms, atom_coords, atom_masses, atom_masses_fac, scale_freq=1.0, debug_print=False):
    """
    on input:
      * k_ind           - index of frequency (integer)
      * k               - the frequency of "k_ind" (string)
      * num_frames      - number of structures to generate along the normal mode (integer)
      * results_path    - name of the subdirectory to which the generated coordinates will be written (string)
      * vibrations      - the normal mode displacement vector of "k_ind" (dict whose key=k and value=OrderedDict with "displacements" data (strin+floats): label(atom),x,y,z)
      * atoms           - atomic labels (list) 
      * atom_masses     - atomic masses (np.ndarray of floats)
      * atom_masses_fac - 1/sqrt(atomic masses) (np.ndarray of floats) 

    on output:
      * a set of xyz files in results_path with molecular geometries 
    """

    if debug_print:
        print('output for k_ind, k = ', k_ind, k)
    vib_coords = [np.array(vibrations[k]["X"]),
                  np.array(vibrations[k]["Y"]),
                  np.array(vibrations[k]["Z"])]
    if (debug_print):
        print('    vib_coords: ', type(vib_coords), np.shape(vib_coords))
        print('    vib_coords: ', vib_coords)
        print('    atom_masses: ', type(atom_masses), np.shape(atom_masses))
        print('    atom_masses: ', atom_masses)
    redmass = reduced_mass(atom_masses, vib_coords)
    vib_max_unscaled = estimate_turning_point(np.float64(k), redmass)
    vib_max = estimate_turning_point(np.float64(k)*float(scale_freq), redmass)

    # for analysis/visualization, increase the range of points:
    vib_max_test = vib_max*4.0
    #probe_step=0.02
    #num_frames_test=round_up_to_odd(vib_max_test/probe_step)
    #if num_frames_test < num_frames:
    #    print('WARNING: , changing num frames for k!', k_ind, k)
    #    num_frames_test=num_frames

    if (debug_print):
        print('  k, k_ind, Mred, vib_max = ', k, k_ind, redmass, vib_max)

    # decide what to use:
    anim_strength= vib_max_test
    num_frames_test=num_frames
    num_frames_used=num_frames

    #print('  k, k_ind, anim_strength, num_frames_used = ', k, k_ind, anim_strength, num_frames_used)
    tmp = []
    allsteps = []
    for i, a in enumerate(atoms):
        ## with a classical turning point limit:
        #anim_strength= vib_max
        #steps = np.linspace(-anim_strength,anim_strength,num_frames)
        ##steps = np.linspace(0,anim_strength,num_frames)

        # increased range for displacements (testing!):
        steps = np.linspace(-anim_strength,anim_strength,num_frames_used)
        if debug_print:
            print('STEPS k_ind, i, a: ', k_ind, i, a, steps)
        tmp.append(steps)


    for nf in range(num_frames_used):
        allsteps.append([tmp[x][nf] for x in range(len(atoms))])
    if (debug_print):
        print('allsteps: ', k_ind, allsteps)  # allsteps is "steps" repeated N times for N atoms

    

    # note: modes numbering from 0
    fout = Path(results_path, 'allstructures_mode_'+str(k_ind)+'.xyz').resolve()
    with open(fout, 'w') as f:
        for nf in range(num_frames_used):
            aa = allsteps[nf]
            # create new coordinates
            # "vib_coords" from ADF are eigenvectors of the force constant matrix in mass-weighted coordinates, so we need to rescale by 1/sqrt(M) to be back at "un-mass-weighted coordinates
            #ax = np.add(atom_coords[0],np.multiply(vib_coords[0],aa[0]))
            #ay = np.add(atom_coords[1],np.multiply(vib_coords[1],aa[1]))
            #az = np.add(atom_coords[2],np.multiply(vib_coords[2],aa[2]))
            dx=np.multiply(atom_masses_fac, np.multiply(vib_coords[0],aa[0]))
            dy=np.multiply(atom_masses_fac, np.multiply(vib_coords[1],aa[1]))
            dz=np.multiply(atom_masses_fac, np.multiply(vib_coords[2],aa[2]))
            dn=np.sqrt(dx**2 + dy**2 + dz**2)
            ax = np.add(atom_coords[0],dx)
            ay = np.add(atom_coords[1],dy)
            az = np.add(atom_coords[2],dz)
            # testing scaling by Mred/sqrt(M)
            #ax = np.add(atom_coords[0],np.multiply(redmass, np.multiply(atom_masses_fac, np.multiply(vib_coords[0],aa[0]))))
            #ay = np.add(atom_coords[1],np.multiply(redmass, np.multiply(atom_masses_fac, np.multiply(vib_coords[1],aa[1]))))
            #az = np.add(atom_coords[2],np.multiply(redmass, np.multiply(atom_masses_fac, np.multiply(vib_coords[2],aa[2]))))
            print('k, k_ind, aa = ', k, k_ind, dx,dy,dz, aa, vib_max)
            f.write('{}\n'.format(len(atoms)))
            f.write('  displacement vector along normal mode of freq {} (from equilibrium): {}; estimated classical turning point={}\n'.format(k,aa,vib_max))
            for i, a in enumerate(atoms):
                f.write('{0}  {1:14.8f}  {2:14.8f}  {3:14.8f}\n'.format(a, ax[i], ay[i], az[i]))

            if (debug_print):
                print('x ', aa, vib_coords[0], np.multiply(vib_coords[0],aa), atom_coords[0], np.add(atom_coords[0],np.multiply(vib_coords[0],aa)))
                print('y ', aa, vib_coords[1], np.multiply(vib_coords[1],aa), atom_coords[1], np.add(atom_coords[1],np.multiply(vib_coords[1],aa)))
                print('z ', aa, vib_coords[2], np.multiply(vib_coords[2],aa), atom_coords[2], np.add(atom_coords[2],np.multiply(vib_coords[2],aa)))
                print("NEW COORDS: ")
                for i, a in enumerate(atoms):
                    print('atoms: ', a, atom_coords[0][i], atom_coords[1][i], atom_coords[2][i], ' --> ', ax[i], ay[i], az[i])

#   also write to separate xyz files:
    for nf in range(num_frames_used):
        fsingleout = Path(results_path, 'geom_'+str(nf)+"_mode_"+str(k_ind)+".xyz").resolve()
        with open(fsingleout, 'w') as f:
            aa = allsteps[nf]
            # create new coordinates
            #ax = np.add(atom_coords[0],np.multiply(vib_coords[0],aa))
            #ay = np.add(atom_coords[1],np.multiply(vib_coords[1],aa))
            #az = np.add(atom_coords[2],np.multiply(vib_coords[2],aa))
            ax = np.add(atom_coords[0],np.multiply(atom_masses_fac, np.multiply(vib_coords[0],aa[0])))
            ay = np.add(atom_coords[1],np.multiply(atom_masses_fac, np.multiply(vib_coords[1],aa[1])))
            az = np.add(atom_coords[2],np.multiply(atom_masses_fac, np.multiply(vib_coords[2],aa[2])))
            f.write('{}\n'.format(len(atoms)))
            f.write('  displacement vector along normal mode of freq {} (from equilibrium): {}; estimated classical turning point={}\n'.format(k,aa,vib_max))
            for i, a in enumerate(atoms):
                f.write('{0}  {1:14.8f}  {2:14.8f}  {3:14.8f}\n'.format(a, ax[i], ay[i], az[i]))




def get_geometry_from_ADF_output(adf_file):
    """
    get information from ADF output:
    * optimized geometry - in Angstrom
    * atom_masses, atom_masses_fac - in amu
    """
    with open(adf_file, "r") as f:
        adf_lines = [x.strip() for x in f.readlines()]
    
        geometry_start=False
        struct_start=False
    
        for iline, line in enumerate(adf_lines):
    
            if geom_start_pattern in line:
                geometry_start=True
                geometry=OrderedDict([("Center",[]), ("X",[]), ("Y",[]), ("Z",[]), ("Mass",[])])
                continue
            if geometry_start and (struct_start_pattern.search(line)):
                struct_start=True
                continue
            if line=="":
                struct_start=False
                continue
            if geometry_start and struct_start:
                l = [_ for _ in re.split(r"\s+", line) if _ !="" ]
                if (len(l) == 8):
                    geometry["Center"].append(l[1])
                    for i,k in zip([2,3,4,7],["X", "Y", "Z", "Mass"]):
                        geometry[k].append(np.float64(l[i]))
                geometries.append(geometry)
    
    geometry = geometries[-1]
    
    atoms = list(geometry.values())[0]
    atom_coords = [np.array(geometry["X"], dtype='d'),
                   np.array(geometry["Y"], dtype='d'),
                   np.array(geometry["Z"], dtype='d')]
    atom_masses = np.array(geometry["Mass"], dtype='d')
    atom_masses_fac = np.divide(1.0, np.sqrt(atom_masses))

    return geometry, atoms, atom_coords, atom_masses, atom_masses_fac
    
def get_vibrations_from_ADF_output(adf_file):
    """
    get information from ADF output:
    * frequency - in cm-1
    * displacement vector = the eigenvector of the mass-weighted Hessian, in Bohr/Angstrom (?)
    """
    with open(adf_file, "r") as f:
        adf_lines = [x.strip() for x in f.readlines()]
    
        nma_start=False
        freq_start=False
    
        for iline, line in enumerate(adf_lines):
    
            if nma_start_pattern in line:
                nma_start=True
                continue
            if nma_start and (freq_start_pattern in line):
                l = [_ for _ in re.split(r"\s+", line) if _ !="" ]
                key = float(l[4])
                key = str(key)
                vibrations[key]= OrderedDict([("Center",[]), ("X",[]), ("Y",[]), ("Z",[])])
                frequencies.append(key)
                freq_start=True
                continue
            if line=="":
                freq_start=False
                continue
            if freq_start and nma_start:
                l = [_ for _ in re.split(r"\s+", line) if _ !="" ]
                if 'Atom' not in l:
                    #print("freq_start and vib_start line ", l)
                    vibrations[key]["Center"].append(l[1])
                    for i,k in zip([2,3,4],["X", "Y", "Z"]):
                        vibrations[key][k].append(float(l[i]))
    return frequencies, vibrations

   

# --- the work starts here --- #

debug_print=False

setup=read_global_setup("global_setup.txt")
Ntest=int(setup["Ntest"])

# hardcoded:
p='coordinates'
adf_file = 'geom.out'

# works with ADF 2022.102:
geom_start_pattern = "G E O M E T R Y"
struct_start_pattern = re.compile(r"\s*X\s*Y\s*Z\s*CHARGE")
geometries = []
nma_start_pattern = "Normal Modes"
freq_start_pattern = "Frequency (cm-1)"
vibrations=OrderedDict()
frequencies=[]

# get structure from ADF output:
geometry, atoms, atom_coords, atom_masses, atom_masses_fac = get_geometry_from_ADF_output(adf_file)
if (debug_print):
    print("ATOMS: ", atoms)
    print("ATOMCOORDS: ", atom_coords)
    print("ATOMMASSES: ", type(atom_masses), np.shape(atom_masses))
    print("ATOMMASSES: ", atom_masses)
    print("ATOMMASSESFAC: ", atom_masses_fac)
    print("ATOMMASSESFAC 9x9: ", np.repeat(atom_masses_fac,3))

# get vibrations from ADF output:
frequencies, vibrations = get_vibrations_from_ADF_output(adf_file)
if (debug_print):
    for k, v in vibrations.items():
        print("VIBRATIONS: ", k, v)

# generate new structures
for i, freq in enumerate(frequencies):
    if scale_freq:
        print("SCALE FREQ: ", sf)
        generate_structures(i, freq, Ntest, p, vibrations, atoms, atom_coords, atom_masses, atom_masses_fac, scale_freq=sf, debug_print=debug_print)
    else:
        generate_structures(i, freq, Ntest, p, vibrations, atoms, atom_coords, atom_masses, atom_masses_fac, debug_print=debug_print)
     

