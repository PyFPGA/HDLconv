#!/bin/bash

set -e

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install .
vhdl2vhdl -v
vhdl2vlog -v
slog2vlog -v
deactivate
