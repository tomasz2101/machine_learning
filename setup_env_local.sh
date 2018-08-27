#!/bin/bash

set -ex

python3 -m venv .venv
source .venv/bin/activate
.venv/bin/pip install pbr
.venv/bin/pip install -r requirements.txt

