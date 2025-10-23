#!/usr/bin/env python
# coding: utf-8

# # Explorations of water clusters: W6_prism

# In[19]:


from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint
import re
import linecache
from IPython.display import display, HTML

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
Chem.Draw.IPythonConsole.ipython_3d = True
from rdkit import rdBase
from rdkit.Chem import rdmolfiles
from rdkit.Chem import rdDetermineBonds
from rdkit.Chem import rdMolAlign
#print(rdBase.rdkitVersion)
import os,time,sys
print( time.asctime())
import py3Dmol
from ipywidgets import interact,fixed,IntSlider
import ipywidgets
sys.path.append(os.getcwd())


# In[20]:


def prepare_fxyz(fxyz):
    '''
    some xyz files in wdbase contain coordinates in engineering notation,
    which is problematic for RdKit,
    so this function makes sure that all coordinates are written as floats
    '''
    engnum=re.compile(r'([0-9]+\.[0-9]*|\.?[0-9]+)([eE][+-][0-9]+)')
    f=open(fxyz, 'r')
    lines=f.readlines()
    f.close()
    newlines=[]
    need_replacement=False
    for line in lines:
        line_with_engnum=re.findall(engnum,line)
        if line_with_engnum:
            need_replacement=True
            newline=[]
            for w in line.strip().split():
                try:
                    ww="{:.9f}".format(float(w))
                except:
                    ww=w
                newline.append(ww)
            newline=f"{'  '.join(newline)}\n"
        else:
            newline=line
        newlines.append(newline)
    if need_replacement:
        with open(fxyz,'w') as f:
            for line in newlines:
                f.write(line)

def from_xyz_to_mol(fxyz, i, assign_index=True):
    '''
    here, the file name has the form "XXX_XXX_XXX.xyz";
    "i" on input refers to the position of geometry index after file name splitting by "_",
    e.g.:
    for "geom_10.xyz", i=1; and for "state_3_mode_5_geom_4.xyz", i=5
    '''
    prepare_fxyz(fxyz)
    comment_line=linecache.getline(str(fxyz), 2)
    tmp=fxyz.stem
    raw_mol = rdmolfiles.MolFromXYZFile(str(fxyz))
    mol = Chem.Mol(raw_mol)
    rdDetermineBonds.DetermineConnectivity(mol)
    if assign_index:
        geom_index = int(tmp.split('_')[i])    
        return geom_index, mol, comment_line
    else:
        return None, mol, comment_line

def grep_energy_from_fxyz(fxyz):
    '''
    energy values should be in the comment line
    '''
    comment_line=linecache.getline(str(fxyz), 2)
    num=re.compile(r'(?<![a-zA-Z:])[-+]?\d*\.?\d+')
    energy=re.findall(num,comment_line)
    return energy[-1]

def prep_numdata(mode_ID, mol_prefix, struc_ID, geom_prefix, geom_ID, data_dir):
    data_file=Path(data_dir, mol_prefix+'_'+mode_ID+'_df.csv').resolve()
    if data_file.is_file():
        df=pd.read_csv(data_file)
        csvfile=str(data_file)
        ds=df[df["filename"] == "geom_"+str(geom_ID)+"_mode_"+str(mode_ID)+".xyz"]
        ds.index=[struc_ID]
    return csvfile, ds


    
def prepare_view(moldict, alignment_option='rmsd', core_smiles='[OH2].[OH2].[OH2].[OH2].[OH2].[OH2]', p=None):
    if p is None:
        p = py3Dmol.view(width=600,height=600)
    p.removeAllModels()
    
    # reference: geomID=5 (equilibrium)
    rmsd_all={}
    ref_mol=moldict[list(moldict)[5]]
    max_rmsd=0.0
    i=0
    colors=('#4aa6ff', '#f65fab', 'spectrum')
    if alignment_option == 'core':
        #core_smiles='[OH2].[OH2].[OH2].[OH2].[OH2].[OH2]'
        #core_smiles='[O].[O].[O].[O].[O].[O]'
        m0=Chem.RemoveHs(ref_mol)
        match_ref_to_core = ref_mol.GetSubstructMatch(Chem.MolFromSmiles(core_smiles))
        for key, mol in moldict.items():
            match_mol_to_core = mol.GetSubstructMatch(Chem.MolFromSmiles(core_smiles))
            AllChem.AlignMol(mol,ref_mol,atomMap=list(zip(match_mol_to_core,match_ref_to_core)))
            mb = Chem.MolToMolBlock(mol)
            p.addModel(mb,'sdf')
        for key, mol in moldict.items():
            p.setStyle({'model':i,},{'stick':{'radius':'0.1','colorscheme':colors[i]}})
            i=i+1
    elif alignment_option == 'rmsd':            
        for key, mol in moldict.items():
            d=AllChem.GetBestRMS(mol,ref_mol)
            rmsd_all[key]=d
            #print("RMSD: ", key, d)
            if d>max_rmsd:
                max_rmsd=d
            mb = Chem.MolToMolBlock(mol)
            p.addModel(mb,'sdf')

        for key, mol in moldict.items():
            p.setStyle({'model':i,},{'stick':{'radius':'0.1','colorscheme':colors[i%len(colors)]}})
            i=i+1
        print("max RMSD:", max_rmsd)
    p.setBackgroundColor('0xeeeeee')
    p.zoomTo()
    return p.show()  



def prepare_view_single(onemol, p=None):
    if p is None:
        p = py3Dmol.view(width=600,height=600)
    p.removeAllModels()
    mb = Chem.MolToMolBlock(onemol)
    #mb.AddBond(order=Chem.rdchem.BondType.HYDROGEN)
    p.addModel(mb,'sdf')
    p.setStyle({'stick':{'radius':'0.1'}})
    p.setBackgroundColor('0xeeeeee')
    p.zoomTo()
    return p   


# In[21]:


parent_dir=Path("../").resolve()

mol_prefix='W6_prism_mp2'
method="nonrel_PBE0_TZ2P"
Nmodes=48

mol_dir_opt=Path(parent_dir, 'coordinates/optimized_'+method+'/'+mol_prefix).resolve()
mol_dir_displ=Path(parent_dir, 'coordinates/trajectories_along_normal_modes/'+mol_prefix+'_'+method).resolve()


# ## Structures

# In[22]:


def from_xyz_to_mol(fxyz, i, assign_index=True):
    '''
    here, the file name has the form "XXX_XXX_XXX.xyz";
    "i" on input refers to the position of geometry index after file name splitting by "_",
    e.g.:
    for "geom_10.xyz", i=1; and for "state_3_mode_5_geom_4.xyz", i=5
    '''
    prepare_fxyz(fxyz)
    comment_line=linecache.getline(str(fxyz), 2)
    tmp=fxyz.stem
    raw_mol = rdmolfiles.MolFromXYZFile(str(fxyz))
    mol = Chem.Mol(raw_mol)
    rdDetermineBonds.DetermineConnectivity(mol)
    if assign_index:
        geom_index = int(tmp.split('_')[i])    
        return geom_index, mol, comment_line
    else:
        return None, mol, comment_line

def prep_data_by_struc_mode(xyz_dir, modeID, geom_prefix=None):
    xyzdirs=[]
    for p in Path(xyz_dir).glob("*"):
        if p.is_file() and p.suffix == ".xyz":
            xyzdirs.append(p)
    return xyzdirs

xyzdirs={}    
for p in Path(mol_dir_displ).glob("*"):
    if p.is_dir() and "mode" in p.name:
        modeID=p.name.replace("mode","")
        xyz_dir=Path(p,"coordinates").resolve()
        xyzdirs[int(modeID)]=prep_data_by_struc_mode(xyz_dir, modeID=modeID, geom_prefix="geom")


# In[23]:


# equilibrium optimized structure:
fxyz=Path(mol_dir_opt,mol_prefix+".xyz").resolve()
geom_index, mol, cl = from_xyz_to_mol(fxyz, 1, assign_index=False)
prepare_view_single(mol)


# In[24]:


# select a vibrational mode to view:
nmode=18


# In[25]:


mol_suppl=xyzdirs[nmode]

selected_mols={}
for fxyz in mol_suppl:
    geom_index, mol, cl = from_xyz_to_mol(fxyz, 1)
    selected_mols[int(geom_index)]=mol

#for k,v in selected_mols.items():
#    print(k, v)


# In[26]:


print("Showing the selected structures after alignment")
prepare_view(selected_mols,alignment_option='rmsd')


# In[ ]:




