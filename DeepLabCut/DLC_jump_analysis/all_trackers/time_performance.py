import csv
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import os
import time_breakdown
 
def time_per(fname):
    w = .9 # bar width
    x = [1, 2, 3, 4, 5] # x-coordinates of your bars
    colors = ['blue', 'red', 'green', 'orange', 'purple']    # corresponding colors
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
    #ax.set_xticklabels(x)
    
    ax.plot(x, y, marker='o'
           #height=[np.mean(yi) for yi in y],
           #yerr=[np.std(yi) for yi in y],    # error bars
           #capsize=12, # error bar cap width in points
           #width=w,    # bar width
           #tick_label=["1/combined", "2", "3", "4", "5"],
           #ylabel=["1/combined", "2", "3", "4", "5"],
           #color=(0,0,0,0),  # face color transparent
           #edgecolor=colors,
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

    
     #plt.legend(['x = x'],bbox_to_anchor =(0.65, 1.25), loc='lower center')
    plt.title("Total Time of Model Construction (10 videos)")
    plt.xlabel("# of animals/models")
    plt.ylabel("time (days)")

    
    for i, j in zip(x, y):
       plt.text(i+.1, j-.2, '({})'.format(j))

    #for xy in zip(x, y):
    #    plt.annotate('(%f, %f)' % xy, xy=xy)

    ax.set_xticklabels(['1/combined', '2', '3', '4', '5'])
    plt.xticks(np.arange(min(x), max(x)+1, 1.0))


    current_dir = os.getcwd()
    print(current_dir)
    os.chdir(current_dir + '/saved_figs')
    figure = plt.gcf()
    figure.set_size_inches(10, 6)
    plt.savefig(fname, dpi=100)
    plt.show()



    # current_dir = os.getcwd()
    # os.chdir(current_dir + '/saved_figs')
    #plt.savefig(fname)

time_per("time_per.png")
