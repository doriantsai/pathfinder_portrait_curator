#! /usr/bin/env python3

"""
rename portrait folders by adding a suffix to all of them in order to guarantee unique folder names in the Portraits directory
"""

import os
from pprint import *

# location of original portrait folders
portrait_dir = '/mnt/c/Users/doria/Documents/UnityModManager/Pathfinder WrathOftheRighteous/GarionPortraitPack'

# additional string prefix/suffix to add onto portrait folder names
pref = 'garion_portrait_pack_'

# get list of portrait folders
portrait_names = sorted(os.listdir(portrait_dir))
pprint(portrait_names)

# add prefix
output_names = [pref + pname for pname in portrait_names]

# rename folders
for i, pname in enumerate(portrait_names):
    pname_path = os.path.join(portrait_dir, pname)
    print(f'changing "{pname}" to "{output_names[i]}"')
    os.rename(pname_path, os.path.join(portrait_dir, output_names[i]))

print('done')
