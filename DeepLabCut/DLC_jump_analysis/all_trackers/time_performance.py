import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import os

def time_per(fname1, fname2):
    w = .9
    x = [1, 2, 3, 4, 5]
    one_animal_model = np.array([.07, 1, .07, 2.5, 3.6]) #time of steps for single model construction
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    #labeling: 10 min/vid --> 100 min (10 vids) --> 1.7 hrs --> .07 days
    #initial training: 1440 min = 24 hrs training --> 1 day
    #refine/extract outlier frames: 10 min/vid --> 100 min (10 vids) --> 1.7 hrs --> .07 days
    #final training: 3600 --> 60 hrs -->  2.5 days
    #total time: 87.4 hrs --> 3.6 days

    #(3.6 days x 24 hrs/day) / (6 hrs/day) = 14 days

    #First graph: Steps and time involved in constructing a single model 
    plt.bar(x, 
           one_animal_model,
           width=w,
           tick_label=["labeling", "initial training", "refining/extracting", "final training", "total"],
           color=colors,
           edgecolor=colors,
           )

    plt.title("Model Time (10 videos)")
    plt.xlabel("Steps")
    plt.ylabel("time (days)")

    current_dir = os.getcwd()
    os.chdir(current_dir + '/saved_figs')

    figure = plt.gcf()
    figure.set_size_inches(8, 6)
    plt.savefig(fname1, dpi=100)
    plt.show()
    plt.close()

    #Second graph: Time to build 5 models corresponding to 5 animals 
    total_time_one_animal = one_animal_model[4]
    two_animal_models = np.multiply(total_time_one_animal, 2)
    three_animal_models = np.multiply(total_time_one_animal, 3)
    four_animal_models = np.multiply(total_time_one_animal, 4)
    five_animal_models = np.multiply(total_time_one_animal, 5)
    y = total_time_one_animal, two_animal_models, three_animal_models, four_animal_models, five_animal_models

    plt.plot(x, y, marker='o')
    plt.xticks(np.arange(min(x), max(x)+1, 1.0), ['1/combined', '2', '3', '4', '5'])
    
    for i, j in zip(x, y):
       plt.text(i+.1, j-.2, '({})'.format(j))


    plt.title("Model Time (10 videos)")
    plt.xlabel("# of animals/models")
    plt.ylabel("time (days)")
    figure = plt.gcf()
    figure.set_size_inches(8, 6)
    plt.savefig(fname2, dpi=100)
    plt.show()
    plt.close()

time_per("time_steps.png", "time_multiple_models.png")
