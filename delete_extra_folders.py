#! /usr/bin/env python3

"""
script to remove extra folders that don't have any portrait images in them
"""

import os
import shutil

# specify folder to look into
root_dir = os.path.abspath('/mnt/c/Users/doria/Documents/UnityModManager/Pathfinder WrathOftheRighteous/Mythical Portraits - Ver.1-448-Ver-1-1678372080/Lexart AI')
# portrait_dir = os.path.abspath('/mnt/c/Users/doria/Documents/Pathfinder_Portraits/Portraits_All')
print(f'portrait directory: {root_dir}')

# list all folders within the main portrait directory
portrait_dirs = sorted(os.listdir(root_dir))

for port in portrait_dirs:
    nfiles = len(os.listdir(os.path.join(root_dir, port)))
    if not (nfiles == 3 or nfiles == 4):
        print(f'removing: {port}')
        shutil.rmtree(os.path.join(root_dir, port))

print('done')

import code
code.interact(local=dict(globals(), **locals()))
