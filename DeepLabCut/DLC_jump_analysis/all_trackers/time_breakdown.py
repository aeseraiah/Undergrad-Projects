import csv
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import os
 
def time_details():
    w = .9 # bar width
    x = [1, 2, 3, 4, 5] # x-coordinates of your bars
    colors = ['blue', 'red', 'green', 'orange', 'purple']    # corresponding colors
    #labeling: 10 min/vid --> 100 min (10 vids) --> 1.7 hrs --> .07 days
    #initial training: 1440 min = 24 hrs training --> 1 day
    #refine/extract outlier frames: 10 min/vid --> 100 min (10 vids) --> 1.7 hrs --> .07 days
    #final training: 3600 --> 60 hrs -->  2.5 days
    #total time: 87.4 hrs --> 3.6 days

    #(3.6 days x 24 hrs/day) / (6 hrs/day) = 14 days

    y = np.array([.07, 1, .07, 2.5, 3.6])
    one_animal_model = np.array([.07, 1, .07, 2.5, 3.6])
    two_animal_models = np.multiply(y, 2)
    three_animal_models = np.multiply(y, 3)
    four_animal_models = np.multiply(y, 4)
    five_animal_models = np.multiply(y, 5)

    fig, ax = plt.subplots()
    ax.bar(x,
           height=[np.mean(yi) for yi in y],
           yerr=[np.std(yi) for yi in y],    # error bars
           capsize=12, # error bar cap width in points
           width=w,    # bar width
           tick_label=["labeling", "initial training", "refining/extracting", "final training", "total"],
           color=(0,0,0,0),  # face color transparent
           edgecolor=colors,
         #ecolor=colors,    # error bar colors; setting this raises an error for whatever reason.
         )

    # for i in range(len(x)):
    #     #distribute scatter randomly across whole width of bar
    #     a = y[i]
    #     ax.scatter(x[i] + np.random.random(a[0:5].size) * w - w / 2, a[0:5], color=colors[i], marker='.')
    #     ax.scatter(x[i] + np.random.random(a[5:10].size) * w - w / 2, a[5:10], color=colors[i], marker = "s")


    # box = ax.get_position()
    # ax.set_position([box.x0, box.y0 + box.height * 0.1,
    #                 box.width, box.height * 0.9])

    # # Put a legend below current axis
    # ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
    #         fancybox=True, shadow=True, ncol=5)

    
    plt.title("Step Time (10 videos)")
    plt.xlabel("Steps")
    plt.ylabel("time (days)")
    #plt.legend(['x = x'],bbox_to_anchor =(0.65, 1.25), loc='lower center')
    
    # plt.show()
    # current_dir = os.getcwd()
    # os.chdir(current_dir + '/saved_figs')
    #plt.savefig(fname)

time_details()
