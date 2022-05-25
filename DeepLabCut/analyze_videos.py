#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:04:37 2019

@author: alex
"""

import os

#import deeplabcut

def getsubfolders(folder):
    ''' returns list of subfolders '''
    return [os.path.join(folder,p) for p in os.listdir(folder) if os.path.isdir(os.path.join(folder,p))]

#project='ComplexWheelD3-12-Fumi-2019-01-28'
project='Folder 1'

shuffle=1

#prefix='/home/alex/DLC-workshopRowland' #Deeplabcut folder #\Users\7teal\Coding Projects\Undergrad-Projects\DeepLabCut\merged
prefix='/Users/7teal/Coding Projects/Undergrad-Projects/DeepLabCut/merged'

projectpath=os.path.join(prefix,project)
config=os.path.join(projectpath,'config.yaml')

print("projectpath:", projectpath)
print("\nconfig:", config, "\n")

#basepath='/home/alex/BenchmarkingExperimentsJan2019' #data'
basepath='/Users/7teal/Coding Projects/Undergrad-Projects/DeepLabCut/merged' #data'

'''

Imagine that the data (here: videos of 3 different types) are in subfolders:
    /January/January29 ..
    /February/February1
    /February/February2

    etc.

'''

subfolders=getsubfolders(basepath)
for subfolder in subfolders: #this would be January, February etc. in the upper example
    print("Starting analyze data in:", subfolder)
    subsubfolders=getsubfolders(subfolder)
    for subsubfolder in subsubfolders: #this would be Febuary1, etc. in the upper example...
        print("Starting analyze data in subfolder:", subsubfolder, "\n")
        #for vtype in ['.mp4','.m4v','.mpg']:
            #deeplabcut.analyze_videos(config,[subsubfolder],shuffle=shuffle,videotype=vtype,save_as_csv=True)
