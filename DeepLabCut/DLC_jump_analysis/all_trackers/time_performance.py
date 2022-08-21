import csv
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import os
import time_breakdown
 
def time_per(fname):
    w = .9
    x = [1, 2, 3, 4, 5]
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    #labeling: 10 min/vid --> 100 min (10 vids) --> 1.7 hrs --> .07 days
    #initial training: 1440 min = 24 hrs training --> 1 day
    #refine/extract outlier frames: 10 min/vid --> 100 min (10 vids) --> 1.7 hrs --> .07 days
    #final training: 3600 --> 60 hrs -->  2.5 days
    #total time: 87.4 hrs --> 3.6 days
    #(3.6 days x 24 hrs/day) / (6 hrs/day) = 14 days

    one_animal_model  = time_breakdown.y
    total_time_one_animal = one_animal_model[4]
    print(total_time_one_animal)
    two_animal_models = np.multiply(total_time_one_animal, 2)
    print(two_animal_models)
    three_animal_models = np.multiply(total_time_one_animal, 3)
    print(three_animal_models)
    four_animal_models = np.multiply(total_time_one_animal, 4)
    print(four_animal_models)
    five_animal_models = np.multiply(total_time_one_animal, 5)
    print(five_animal_models)
    y = total_time_one_animal, two_animal_models, three_animal_models, four_animal_models, five_animal_models

    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_xticklabels(['1/combined', '2', '3', '4', '5'])
    plt.xticks(np.arange(min(x), max(x)+1, 1.0))
    
    for i, j in zip(x, y):
       plt.text(i+.1, j-.2, '({})'.format(j))

    current_dir = os.getcwd()
    plt.title("Total Time of Model Construction (10 videos)")
    plt.xlabel("# of animals/models")
    plt.ylabel("time (days)")
    #os.chdir(current_dir + '/saved_figs')
    figure = plt.gcf()
    figure.set_size_inches(10, 6)
    plt.savefig(fname, dpi=100)
    plt.show()
    plt.close()

time_per("time_per.png")
