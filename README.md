# Operator Properties and Mathematical Structure of Nonlocal Morphing

Theory + code for **operator-level nonlocal morphing (density imprint)**:
\[
U_\alpha = \exp\!\big(i\,\alpha\,(W * |\psi|^2)\big)
\]
including operator properties, mean-field reduction, error bounds, and **reproducible figures**.

<!-- Add the Zenodo DOI badge here after the first release -->
<!-- [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX) -->

## Quick start
```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
# .venv\Scripts\activate

pip install -r envs/requirements.txt
python code/generate_figures_png.py
# outputs → figures/
code/                 # simulation + plotting scripts
envs/requirements.txt # Python deps
figures/              # exported PNG/PDF (samples)
data/README.md        # where large datasets live (Zenodo)
CITATION.cff
LICENSE               # MIT (code)
LICENSE-CC-BY-4.0     # CC BY 4.0 (text/figures)
