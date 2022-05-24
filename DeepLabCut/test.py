from __future__ import print_function
import sys
print(int(sys.argv[1]), len(sys.argv))

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

print(projectpath)
print(config)

