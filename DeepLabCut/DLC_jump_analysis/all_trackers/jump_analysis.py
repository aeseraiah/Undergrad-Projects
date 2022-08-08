import csv
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import os

#NOTE: change nose_directory in for loop to rump_directory to make the other bar graph
pull_path_nose_directory = "C:/Users/7teal/Coding Projects/Undergrad-Projects/DeepLabCut/DLC_jump_analysis/all_trackers/"
nose_directory = "csv_files"
rump_directory = "csv_rump_files"
pull_path_rump_directory = "C:/Users/7teal/Coding Projects/Undergrad-Projects/DeepLabCut/DLC_jump_analysis/all_trackers/"


def main(full_path, relative_path):
    # for i in nose_csv_list:
    #     nose = pd.read_csv(i)
    #     nose_df = pd.DataFrame(nose)
    #     nose_values = nose_df.columns.values.astype(float)
    current_dir = os.getcwd()
    os.chdir(current_dir + '/' + relative_path)
    # arr = {}
    # new_current_dir = os.getcwd()
    
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        file_count = len(files)
    
    print(file_count)

    dataframes_list = []

    for i in range(file_count):
        temp_df = pd.read_csv(files[i])
        dataframes_list.append(temp_df)
        
    for dataset in dataframes_list:
        print(dataset)























    # for filename in os.listdir(new_current_dir):
    #     nose = pd.read_csv(filename)
    #     nose_df = pd.DataFrame(nose)
    #     nose_values = nose_df.columns.values.astype(float)
        #print(type(nose_values))
        #print(nose_values)
        # arr[filename] = nose_values(filename)
        # print(arr)
        # for i in nose_values:
        #      arr[i] = nose_values


    #print(nose_values)


main(pull_path_nose_directory, nose_directory)



    # nose = pd.read_csv(single_tracker_nose_csv)
    # nose_df = pd.DataFrame(nose)
    # nose_values = nose_df.columns.values.astype(float)
    # #print("nose_values:\n", nose_values)
    # Ms22_values = nose_values[0:5]
    # print("Ms22_values:\n", Ms22_values)
    # Rear5_values = nose_values[5:10]
    # print("Rear5_values:\n", Rear5_values)

    # rump = pd.read_csv(single_tracker_rump_csv)
    # rump_df = pd.DataFrame(rump)
    # rump_values = rump_df.columns.values.astype(float)
    # #print("rump_values:\n", rump_values)




    # w = 0.1  # bar width
    # x = [1] # x-coordinates of your bars
    # colors = [(0, 0, 1, 1), (1, 0, 0, 1)]    # corresponding colors
    # y2 = Ms22_values#, Rear5_values
    # #y = [Ms22_values,Rear5_values]
    # y = [nose_values]
    # print(y)
 

    # fig, ax = plt.subplots()
    # ax.bar(x,
    #        height=[np.mean(yi) for yi in y],
    #        yerr=[np.std(yi) for yi in y],    # error bars
    #        capsize=12, # error bar cap width in points
    #        width=w,    # bar width
    #        tick_label=["Rear5/Ms22","Ms21"],#,"Combined", "RC1"],
    #        color=(0,0,0,0),  # face color transparent
    #        edgecolor=colors,
    #      #ecolor=colors,    # error bar colors; setting this raises an error for whatever reason.
    #      )

    # for i in range(len(x)):
    #     #distribute scatter randomly across whole width of bar
    #     a = y[i]
    #     ax.scatter(x[i] + np.random.random(a[0:5].size) * w - w / 2, a[0:5], color=colors[i])
    #     ax.scatter(x[i] + np.random.random(a[5:10].size) * w - w / 2, a[5:10], color=colors[i+1])
    #     print(y[0])

    # plt.show()
    # #plt.save()




#main(nose_file, rump_file)