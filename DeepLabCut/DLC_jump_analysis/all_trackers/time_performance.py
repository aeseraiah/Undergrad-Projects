import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import os

def time_per(fname1, fname2, fname3):
    w = .9
    x = [1, 2, 3, 4, 5, 6]
    #one_animal_model = np.array([.07, 1, .07, 2.5, 3.6]) #time of steps for single model construction (10 vids)
    #combined_animal_model = np.array([.11, 1, .11, 2.5, 3.72]) #16 vids for combined model
    one_animal_model = np.array([.08, 1, .08, 2.5, .06, 3.7]) #12 vids for single model 
    colors = ['fuchsia', 'red', 'green', 'orange', 'purple', 'blue']
    #labeling: 10 min/vid --> 120 min (12 vids) --> 2 hrs --> .08 days
    #initial training: 1440 min = 24 hrs training --> 1 day
    #refine/extract outlier frames: 10 min/vid --> 120 min (12 vids) --> 2 hrs --> .08 days
    #final training: 3600 --> 60 hrs -->  2.5 days
    #total time: 3.7 days

    #(3.7 days x 24 hrs/day) / (6 hrs/day) = 14 days

    #First graph: Steps and time involved in constructing a single model 
    plt.bar(x, 
           one_animal_model,
           width=w,
           tick_label=["labeling", "initial training", "refining/extracting", "final training", "automated labels", "total"],
           color=colors,
           edgecolor=colors,
           zorder=3
           )

    plt.grid(color='grey', linestyle='-', linewidth=.1, axis='y')

    #plt.title("Model Time (12 training videos)")
    plt.xlabel("Steps")
    plt.ylabel("time (days)")

    current_dir = os.getcwd()
    os.chdir(current_dir + '/saved_figs')

    figure = plt.gcf()
    figure.set_size_inches(6, 6)
    plt.ylim(0,4.5)
    plt.savefig(fname1, dpi=100)
    #plt.show()
    plt.close()

    #Second graph: Time to build 5 models corresponding to 5 animals 
    total_time_one_animal = np.round((one_animal_model[5] + .06), 2) 

    analysis_time = np.round(total_time_one_animal, 2)
    analysis_time_2 = np.round((total_time_one_animal + one_animal_model[4]), 2)
    analysis_time_3 = np.round((analysis_time_2 + one_animal_model[4]), 2)
    analysis_time_4 = np.round((analysis_time_3 + one_animal_model[4]), 2)
    analysis_time_5 = np.round((analysis_time_4 + one_animal_model[4]), 2)
    two_animal_models = np.round((total_time_one_animal*2), 2)
    three_animal_models = np.round((total_time_one_animal*3), 2)
    four_animal_models = np.round((total_time_one_animal*4), 2)
    five_animal_models = np.round((total_time_one_animal*5), 2)

    # analysis_arr = []
    # for x in range(1,6):
    #     analysis_arr.append(analysis_time)

    # new_arr = []
    # nn_arr = [1,2,3,4,5]

    # for i in analysis_arr:
    #     x = np.arange(1,6)
    #     new_arr.append(i*x[i])

    #     # for j in range(1,6):
    #     #     new_arr.append(i*j)

    # print(new_arr)

    y = total_time_one_animal, two_animal_models, three_animal_models, four_animal_models, five_animal_models


    y2 = [total_time_one_animal, total_time_one_animal, total_time_one_animal, total_time_one_animal, total_time_one_animal]
    new_y = [analysis_time, analysis_time_2, analysis_time_3, analysis_time_4, analysis_time_5]
    print(new_y)
    print(y)

    x2 = [1, 2, 3, 4, 5]
    plt.plot(x2, y, marker='.')
    plt.plot(x2,new_y)
    plt.legend(['Single Models', 'Combined Model'], loc='upper left')
    plt.xticks(np.arange(min(x2), max(x2)+1, 1.0), ['1', '2', '3', '4', '5'])
    
    for i, j in zip(x2, y):
       plt.text(i-.05, j-.7, '{}'.format(j))


    plt.grid(color='grey', linestyle='-', linewidth=.1)
    plt.ylim(0,20)
    #plt.title("Model Time (12 training videos)")
    plt.xlabel("Num. of rats")
    plt.ylabel("Total Analysis Time (days)")
    figure = plt.gcf()
    figure.set_size_inches(14, 10)
    plt.savefig(fname2, dpi=100)
    #plt.show()
    plt.close()


########################
    y3 = np.random.uniform(low=10, high=15, size=(20))
    print(y3[9])
    print(y3[12])
    y3[10] = 100
    y3[11] = 100
    y4 = [0,0,0,0]
    x3 = np.arange(1,21)
    #x3[10]
    np.random.seed(0)
    y5 = np.random.uniform(low=10, high=15, size=(20))
    y3[0] = y5[0]

    plt.plot(x3, y3, marker='.', linewidth=2.5) #--> jumpy/blue
    plt.plot(x3, y5, marker='.', linewidth=3)
    plt.legend(['Jumpy', 'Correct'])
    #plt.xticks(np.arange(min(x3), max(x3)+1, 1.0), ['1', '2', '3', '4'])
    

    plt.axhline(y=87, color='r', linestyle='--')
    plt.grid(color='grey', linestyle='-', linewidth=.1)
    plt.ylim(0,120)
    #plt.xlabel("")
    
    plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)


    plt.ylabel("Abs coordinate diff. between frames (pixels)")
    plt.xlabel("Frame difference: n - (n-1)")
    figure = plt.gcf()
    figure.set_size_inches(10,6)
    plt.savefig(fname3, dpi=100)
    plt.show()
    plt.close()

time_per("time_steps.png", "time_multiple_models.png", "frame_difference.png")
