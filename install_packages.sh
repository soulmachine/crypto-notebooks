#!/bin/bash
sudo /opt/conda/bin/conda install -c conda-forge vaex
sudo /opt/conda/bin/conda install -c conda-forge swifter
sudo /opt/conda/bin/pip3 install 'pymars[distributed]'
sudo /opt/conda/bin/conda install -c bjrn pandarallel
sudo /opt/conda/bin/conda install -c conda-forge modin
sudo /opt/conda/bin/pip3 install nbdev
