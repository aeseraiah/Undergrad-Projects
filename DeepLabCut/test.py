from __future__ import print_function
import sys
#print(int(sys.argv[1]), len(sys.argv))

list = [['t1'], ['t2'], ['t3']]
for x in list[2]:
    #print(x)
    break

import os

model=int(sys.argv[1])

Projects=[['t1'], ['t2'], ['t3']]

shuffle=1

prefix='/content/gdrive/MyDrive'

for project in Projects[model]:
    projectpath=os.path.join(prefix,project)
    config=os.path.join(projectpath,'config.yaml')

print("projectpath:", projectpath)
print("config:", config)

###
def getsubfolders(folder):
    ''' returns list of subfolders '''
    return [os.path.join(folder,p) for p in os.listdir(folder) if os.path.isdir(os.path.join(folder,p))]

project='ComplexWheelD3-12-Fumi-2019-01-28'

shuffle=1

prefix='/home/alex/DLC-workshopRowland'

projectpath=os.path.join(prefix,project)
config=os.path.join(projectpath,'config.yaml')

basepath='/home/alex/BenchmarkingExperimentsJan2019' #data'


