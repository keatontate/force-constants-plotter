#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 13:13:20 2022

plots FORCE_CONSTANTS as a heatmap using numpy arrays and matplotlib

@author: keaton
"""
import os
import numpy as np
from matplotlib import pyplot as plt

# Generate the forceConstants matrix

with open('FORCE_CONSTANTS') as f:
    line = f.readline()
    
blockSize = int(line.strip().split(' ')[0])

myArray = np.genfromtxt('FORCE_CONSTANTS', skip_header=2, autostrip=True, invalid_raise=False)

arrayShape = np.shape(myArray)
arraySize = int(np.sqrt(arrayShape[0] * arrayShape[1]))

columnArraysList = np.split(myArray, blockSize, axis=0)

forceConstants = abs(np.hstack(columnArraysList)) # we use absolute value because we're only interested in the magnitude of the displacement from 0


# Get minimum value of forceConstants matrix, count all elements above this threshold (for comparison later)

thresh = forceConstants.min()

numElements = len(forceConstants.flatten())

aboveThresh = [i for i in forceConstants.flatten() > thresh]
aboveThresh = np.asarray(aboveThresh)
aboveThresh = np.sum(aboveThresh)

aboveThreshRatio = aboveThresh / numElements


# Plotting section

cwd = str(os.getcwd())
cwd = cwd[-19:]

fig, ax = plt.subplots(figsize=(15,10))

im = ax.matshow(forceConstants)
plotTitle = f"Force Constants - {cwd} - Ratio Above Threshold: {aboveThreshRatio} - Threshold: {thresh}"
ax.set_title(plotTitle)
fig.colorbar(im)

plt.savefig(f"{cwd[1:]}_AboveThreshRatio-{aboveThreshRatio}_Thresh-{thresh}.png")