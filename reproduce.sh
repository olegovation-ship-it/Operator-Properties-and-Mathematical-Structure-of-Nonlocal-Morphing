#!/usr/bin/env bash
set -e
python -m venv .venv
source .venv/bin/activate
pip install -r envs/requirements.txt
python code/generate_figures_png.py
