Additional content:

* **W6_vibrations/**
  * `W6_all_freqs.ods` - a spreadsheet with harmonic frequencies calculated in this work 
  * **coordinates/** - initial (literature) structures, optimized equilibrum structures and "distorted" structures along each vibrational mode for each isomer (structures in XYZ format)
  * **scripts_templates/** - chemistry calculations - scripts, templates
  * **notebooks/** - a jupyter notebook demonstrating the structures of W6 prism isomer; can be adapted to other isomers; 


* **W6_tunneling/**
  * **coordinates/** - structures along each tunneling pathway (structures in XYZ format)
  * **scripts_templates/** - chemistry calculations - scripts, templates
  * **notebooks/** - jupyter notebooks demonstrating the structures

* `conda_env.yml` - conda environment allowing to run the analyses in jupyter notebooks;
  it can be used as follows:

  ```
  mamba env create -n W6_isomers_env -f conda_env.yml
  conda activate W6_isomers_env
  cd notebooks
  jupyter notebook W6_prism.ipynb
  ```

   
