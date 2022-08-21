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

    fig, ax = plt.subplots()
    ax.bar(x, y,
           width=w,
           tick_label=["labeling", "initial training", "refining/extracting", "final training", "total"],
           color=colors,
           edgecolor=colors,
         )

    plt.title("Model Time")
    plt.xlabel("Steps")
    plt.ylabel("time (days)")

    current_dir = os.getcwd()
    os.chdir(current_dir + '/saved_figs')
    
    figure = plt.gcf()
    figure.set_size_inches(8, 6)
    plt.savefig(fname, dpi=100)
    plt.show()
    plt.close()


time_details("time_steps.png")
