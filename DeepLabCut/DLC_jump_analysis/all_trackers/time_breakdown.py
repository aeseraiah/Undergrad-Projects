import csv
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import os

y = np.array([.07, 1, .07, 2.5, 3.6])
 
def time_details(fname):
    w = .9
    x = [1, 2, 3, 4, 5]
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    #labeling: 10 min/vid --> 100 min (10 vids) --> 1.7 hrs --> .07 days
    #initial training: 1440 min = 24 hrs training --> 1 day
    #refine/extract outlier frames: 10 min/vid --> 100 min (10 vids) --> 1.7 hrs --> .07 days
    #final training: 3600 --> 60 hrs -->  2.5 days
    #total time: 87.4 hrs --> 3.6 days

    #(3.6 days x 24 hrs/day) / (6 hrs/day) = 14 days
    one_animal_model = np.array([.07, 1, .07, 2.5, 3.6])
    two_animal_models = np.multiply(y, 2)
    three_animal_models = np.multiply(y, 3)
    four_animal_models = np.multiply(y, 4)
    five_animal_models = np.multiply(y, 5)

    fig, ax = plt.subplots()
    ax.bar(x,
           height=[np.mean(yi) for yi in y],
           yerr=[np.std(yi) for yi in y], 
           capsize=12, 
           width=w,
           tick_label=["labeling", "initial training", "refining/extracting", "final training", "total"],
           color=(0,0,0,0),
           edgecolor=colors,
         )

    
    plt.title("Step Time (10 videos)")
    plt.xlabel("Steps")
    plt.ylabel("time (days)")
    current_dir = os.getcwd()
    os.chdir(current_dir + '/saved_figs')
    figure = plt.gcf()
    figure.set_size_inches(10, 6)
    plt.savefig(fname, dpi=100)
    plt.show()
    plt.close()


time_details("time_steps.png")
