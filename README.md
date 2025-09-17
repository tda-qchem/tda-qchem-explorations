# tda-qchem-explorations
A collection of examples accompanying the TDA-Qchem book (scratch repository).


## Contributing

### Text

* Add a markdown file with example description to `docs`; a template is available: `docs/templates/doc.md`:

```
# copy template
cd docs
cp docs/templates/doc.md MY-EXAMPLE.md
# edit MY-EXAMPLE.md
cd ..
``` 

* If screenshot(s) and/or video(s) are demonstrated, add them to `docs/screenshots/MY-EXAMPLE/` and/or `docs/videos/MY-EXAMPLE/`.

* Add a link to `MY-EXAMPLE.md` in `docs/index.md`.

* Add state files to `state_files/`.
    * Make sure you are using relative links to `.vti` data files

* Add Python scripts to `python/`.
    * Make sure you are using relative links to `.vti` data files

* Check if all is nicely rendered

```
mkdocs serve
```

* It might be helpful to work in conda environment:

```
conda create -n mkdocs mkdocs mkdocs-material mkdocs-video
conda activate mkdocs
```

### Data

Create the content of the `data` directory:

* Create a corresponding directory in `data`; with the following subdirectories:
  `QC-software/MODEL_USED/inputs`, `QC-software/MODEL_USED/outputs`, `vti`, `ttk`

  * gosia (decision Sept/2025): vti files are not on git due to size; they can be downloaded from Zenodo (with links provided in docs)

* Add molecular geometry (XYZ in Angstrom and CSV in Bohr) to `coordinates` 


