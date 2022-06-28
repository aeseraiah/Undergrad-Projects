import numpy as np
import matplotlib.pylab as plt


plt.rcParams['figure.figsize'] = (15,15) # Pick something here, bigger than (6.0,4.0)
plt.rcParams['font.size'] = 25           # pick something bigger than 10 
plt.rcParams['lines.markersize'] = 7

import csv 

d = np.zeros( (1000,6) ); # I already know the size this time. 
n = 0; 
with open( "features.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',' ); 
    for row in csv_reader: 
        j = 0;
        for dat in row:
            d[n,j] = float( dat ); 
            j = j+1;
        n = n+1;