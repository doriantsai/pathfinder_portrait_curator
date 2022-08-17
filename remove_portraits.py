#! /usr/bin/env python

"""
Script to remove Pathfinder Portraits that do not match the correct aspect ratio/pixel dimensions
Author: Dorian Tsai
Date: 2022 Aug 17
"""

import os
import shutil
import machinevisiontoolbox as mvt

# valid portrait dimensions:
# https://pathfinder-kingmaker.fandom.com/wiki/Custom_Portraits
# Small       width: 185px, height: 242px;
# Medium      width: 330px, height: 432px;
# Fulllength  width: 692px, height: 1024px;

DELETE_INCONSISTENT_FOLDERS = True

class Portrait:
    # class for Portrait that is defined by image size and name
    def __init__(self, width=None, height=None, name=None):
        self.width = width
        self.height = height
        self.name = name

def check_size(image, portrait):
    # image is numpy array 
    # image.shape = (height, width, channels) = (tuple)
    # portrait is portrait object
    # check if image size matches portrait size
    [height, width, chan] = image.shape
    if (height == portrait.height) and (width == portrait.width):
        return True
    else:
        return False

PortSm = Portrait(width=185, height=242, name='Small.png')
PortMd = Portrait(width=330, height=432, name='Medium.png')
PortLg = Portrait(width=692, height=1024, name='Fulllength.png')

# specify folder to look into
portrait_dir = os.path.abspath('/mnt/c/Users/doria/AppData/LocalLow/Owlcat Games/Pathfinder Wrath Of The Righteous/Portraits')
# portrait_dir = os.path.abspath('/mnt/c/Users/doria/Documents/Pathfinder_Portraits/Portraits_All')
print('portrait directory:')
print(portrait_dir)

# get list of all portrait folders
plist = os.listdir(portrait_dir)
print('list of portrait folders')
print(f'len of plist: {len(plist)}')
# for p in plist:
#     print(p)

# folder structure:
# within portrait_dir, each "portrait" has a set images:
#   Small.png
#   Medium.png
#   Fulllength.png

# for each folder in plist,
#   get a list of all the files in the folder
#   there should be 3, and they should be called Small.png, Medium.png, Fulllength.png
#   then get the image dimensions of all 3 and compare them to the Portrait dimensions
#   save these indices as a list

# print('number of files')
p_ok = []
p_fail = []
name_check_fail = []
for i, p in enumerate(plist):
    pfiles = os.listdir(os.path.join(portrait_dir, p))
    # print(len(pfiles))
    if not (PortSm.name in pfiles) or \
        not (PortMd.name in pfiles) or \
            not (PortLg.name in pfiles):
        name_check_fail.append(i)

    portrait_pass = 0
    for f in pfiles:
        # read in image and check image dimensions
        # NOTE could probably do this faster/more efficiently just using numpy directly
        im, file = mvt.iread(os.path.join(portrait_dir, p, f))
        if f == PortSm.name:
            if check_size(im, PortSm):
                portrait_pass += 1
        if f == PortMd.name:
            if check_size(im, PortMd):
                portrait_pass += 1
        if f == PortLg.name:
            if check_size(im, PortLg):
                portrait_pass += 1

    # only if portrait_pass matches all over the iteration of the 3 pfiles, then we keep the portrait
    if portrait_pass == 3:
        p_ok.append(i)
    else:
        p_fail.append(i)

# print(len(plist))
# print(len(p_ok))
# print(len(p_fail))
# print(len(p_ok) + len(p_fail))

# print names of failed name checks to manually fix (numbers are small)
print('name check fail:')
for n in name_check_fail:
    print(plist[n])

# report list of all portrait folders that don't match the regime
# delete all of these folders with user input

print('folders to remove:')
for p in p_fail:
    print(plist[p])

if DELETE_INCONSISTENT_FOLDERS:
    print('removing inconcistent portraits')
    for p in p_fail:
        if os.path.isdir(os.path.join(portrait_dir, plist[p])):
            # WARNING: permanently deletes the folder with all its contents!
            shutil.rmtree(os.path.join(portrait_dir, plist[p]))

# # handy debug code
# import code
# code.interact(local=dict(globals(), **locals()))