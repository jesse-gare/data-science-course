#!/usr/bin/env python
"""
Gather some course content.
"""

import os

# Github repositories to get:
repos = [
    "https://github.com/jakevdp/WhirlwindTourOfPython",
    "https://github.com/jakevdp/PythonDataScienceHandbook",
    "https://github.com/pzwang/bokeh-dashboard-webinar",
    "https://github.com/omartinsky/QuantAndFinancial",
    "https://github.com/QuuxZebula/quanty-python",
    "https://github.com/martin-gorner/tensorflow-mnist-tutorial",
]

# Get the resources:
for repo in repos:
    command = "git clone {}".format(repo)
    print(command)
    os.system(command)

# Get a tool for removing outputs from notebooks:
os.system("conda install -c conda-forge nbstripout")

# Clean the outputs form the notebooks:
root = os.getcwd()
for path, sub_paths, file_names in os.walk(root):
    for name in file_names:
        if name.endswith(".ipynb"):
            full_name = os.path.join(root, path, name)
            command = "nbstripout {}".format(full_name)
            print(command)
            os.system(command)
