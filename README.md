# Operator Properties and Mathematical Structure of Nonlocal Morphing

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17557943.svg)](https://doi.org/10.5281/zenodo.17557943)

Theory + code for **operator-level nonlocal morphing (density imprint)**:
\( U_\alpha = \exp\!\big(i\,\alpha\,(W * |\psi|^2)\big) \)
including operator properties, mean-field reduction, error bounds, and **reproducible figures**.

## Quick start
~~~bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
# .venv\Scripts\activate

pip install -r envs/requirements.txt
python code/generate_figures_png.py
# outputs → figures/
~~~

## Repository layout
~~~
code/                 # simulation + plotting scripts
envs/requirements.txt # Python deps
figures/              # exported PNG/PDF (samples)
data/README.md        # where large datasets live (Zenodo)
CITATION.cff
LICENSE               # MIT (code)
LICENSE-CC-BY-4.0     # CC BY 4.0 (text/figures)
~~~

## How to cite

**APA**  
Panasenko, D. (2025). *Unitary Morphing via Density Imprint (repro pack)* (v1.0.0) [Software]. Zenodo. 
[![DOI](https://zenodo.org/badge/DOI/<PREPRINT_DOI>.svg)](https://doi.org/<PREPRINT_DOI>)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17557943.svg)](https://doi.org/10.5281/zenodo.17557943)

**BibTeX**
~~~bibtex
@software{panasenko_2025_unitary_morphing_v1_0_0,
  author  = {Panasenko, Dmytro},
  title   = {Unitary Morphing via Density Imprint (repro pack)},
  year    = {2025},
  version = {1.0.0},
  doi     = {10.5281/zenodo.17557943},
  url     = {https://doi.org/10.5281/zenodo.17557943}
}
~~~
