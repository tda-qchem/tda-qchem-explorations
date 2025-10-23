#!/usr/bin/env python
# coding: utf-8

# # Explorations of water clusters: tunneling pathways in W6_prism

# In[ ]:


from pathlib import Path
import pandas as pd
import numpy as np
from scipy import linalg
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


# ### About: analysis of geared and antigeared rotations of a pair of water molecules 
# 
# Based on https://www.science.org/doi/10.1126/science.aae0012 (`richardson.etal_s_2016`)

# In[ ]:


def numdata_from_geoms(fxyz):
    if fxyz.is_file():
        raw_mol = rdmolfiles.MolFromXYZFile(str(fxyz))
    mol = Chem.Mol(raw_mol)
    rdDetermineBonds.DetermineConnectivity(mol)
    if assign_index:
        geom_index = int(tmp.split('_')[i])    
        return geom_index, mol, comment_line
    else:
        return None, mol, comment_line

    
def create_moldict_from_xyz_files(coordinates_dir, removeHs=False, name_from_filename=False, idx_pos=0):
    moldict = {}
    for id, inp in enumerate(Path(coordinates_dir).glob(f'*.xyz')):
        mol = rdmolfiles.MolFromXYZFile(str(inp))
        if name_from_filename:
            name = inp.stem.split('_')[idx_pos]
        else:
            name = id
        moldict[int(name)] = mol
    md_sorted={k: v for k, v in sorted(list(moldict.items()))}
    return md_sorted
       

def prep_numdata(data_file, mol_prefix):
    if data_file.is_file():
        df=pd.read_csv(data_file)
        tmp=df["FILE"].str.split('/',expand=True)[1]
        strucID=tmp.str.split('_',expand=True)[3]
        df["strucID"]=strucID
        df["strucID"]=df["strucID"].astype('int32')
    return df

def get_geomdata_single(m):
    oxr={}
    hyr={}
    o_id=[]
    h_id=[]
    mc=m.GetConformer()
    for i, atom in enumerate(m.GetAtoms()):
        if atom.GetAtomicNum() == 8:
            o_id.append(atom.GetIdx())
            o_mass=atom.GetMass()
            f=np.sqrt(o_mass)
            ox=f*mc.GetAtomPosition(i).x
            oy=f*mc.GetAtomPosition(i).y
            oz=f*mc.GetAtomPosition(i).z
            oxr[i]=np.array([ox,oy,oz],dtype=float)

        elif atom.GetAtomicNum() == 1:
            h_id.append(atom.GetIdx())
            h_mass=atom.GetMass()
            f=np.sqrt(h_mass)
            hx=f*mc.GetAtomPosition(i).x
            hy=f*mc.GetAtomPosition(i).y
            hz=f*mc.GetAtomPosition(i).z
            hyr[i]=np.array([hx,hy,hz],dtype=float)
    return oxr,hyr,o_id,h_id


def get_geomdata(moldict):
    data={}
    oxr={}
    hyr={}
    path_sum=0
    data[1]=path_sum
    for k, m in moldict.items():
        oxr[k],hyr[k],o_id,h_id=get_geomdata_single(m)
    oxr2={int(i):{} for i in o_id}
    hyr2={int(i):{} for i in h_id}
    for k1, v1 in oxr.items():
        for k2, v2 in v1.items():
            oxr2[k2][k1]=v2
    for k1, v1 in hyr.items():
        for k2, v2 in v1.items():
            hyr2[k2][k1]=v2
    for k, v in oxr2.items():
        path_sum=0
        for i in range(1, len(v)+1):
            if i>1:
                lo=v[i]-v[i-1]
                path_sum=path_sum+linalg.norm(lo)
                data[i]=path_sum
    for k, v in hyr2.items():
        path_sum=0
        for i in range(1, len(v)+1):
            if i>1:
                lh=v[i]-v[i-1]
                path_sum=path_sum+linalg.norm(lh)
                data[i]=path_sum
    return data


def from_xyz_to_mol(fxyz, i, assign_index=True):
    '''
    here, the file name has the form "XXX_XXX_XXX.xyz";
    "i" on input refers to the position of geometry index after file name splitting by "_",
    e.g.:
    for "geom_10.xyz", i=1; and for "state_3_mode_5_geom_4.xyz", i=5
    '''
    #prepare_fxyz(fxyz)
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


# In[ ]:


coor_dir=Path("../coordinates").resolve()

coor_p1=Path(coor_dir,"W6_drop1_prep").resolve()
coor_p2=Path(coor_dir,"W6_bifdrop_prep").resolve()

moldict_p1=create_moldict_from_xyz_files(coor_p1,name_from_filename=True, idx_pos=-1)
moldict_p2=create_moldict_from_xyz_files(coor_p2,name_from_filename=True, idx_pos=-1)


# In[ ]:


mols_p1={}
mols_p2={}

def get_moldict(moldir):
    mf=[]
    mols={}
    for p in Path(moldir).glob("*"):
        if p.is_file() and p.suffix == ".xyz":
            mf.append(p)
    #return mf
    for fxyz in mf:
        geom_index, mol, cl = from_xyz_to_mol(fxyz, 3, True)
        mols[int(geom_index)]=mol
    return mols
    
mols_p1=get_moldict(Path(coor_dir, "W6_drop1_prep"))    
mols_p2=get_moldict(Path(coor_dir, "W6_bifdrop_prep"))    
#for k,v in mols_p1.items():
#    print(k, v)


# In[ ]:


geomdata_p1=get_geomdata(moldict_p1)
geomdata_p2=get_geomdata(moldict_p2)


# # structures

# In[ ]:


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


# In[ ]:


print("Showing the selected structures after alignment: path1")
#prepare_view(selected_mols,alignment_option='core',core_smiles='[O].[O].[O].[O].[O].[O]')
prepare_view(mols_p1,alignment_option='rmsd')


# In[ ]:


print("Showing the selected structures after alignment: path2")
#prepare_view(selected_mols,alignment_option='core',core_smiles='[O].[O].[O].[O].[O].[O]')
prepare_view(mols_p2,alignment_option='rmsd')

