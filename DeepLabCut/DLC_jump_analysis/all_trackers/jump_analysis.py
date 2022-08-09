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

def main(full_path, relative_path, fname):
    current_dir = os.getcwd()
    os.chdir(current_dir + '/' + relative_path)

    
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        file_count = len(files)


    dataframes_list = []
    for i in range(file_count):
        temp_df = pd.read_csv(files[i])
        nose_df1 = pd.DataFrame(temp_df)
        nose_values1 = nose_df1.columns.values.astype(float)
        dataframes_list.append(nose_values1)

        
    #for i in dataframes_list:
        #print(i)


    #Combined Model:
    combined_df_values = dataframes_list[0]
    #print("Ms21 values:\n", combined_df_values)

    combined_df_values_Ms22 = combined_df_values[0:5]
    #print("combined_df_values_Ms22:\n", combined_df_values_Ms22)
    combined_df_values_Rear5 = combined_df_values[5:10]
    #print("combined_df_values_Rear5:\n", combined_df_values_Rear5) 


    combined_new_df_values = dataframes_list[1]
    
    #Ms21 Model:
    Ms21_df_values = dataframes_list[2]
    #print("Ms21 values:\n", Ms21_df_values)

    Ms21_values_Ms22 = Ms21_df_values[0:5]
    #print("Ms21_values_Ms22:\n", Ms21_values_Ms22)
    Ms21_values_Rear5 = Ms21_df_values[5:10]
    #print("Ms21_values_Rear5:\n", Ms21_values_Rear5)

    Ms21_new_df_values = dataframes_list[3]


    #Single Models:
    Ms22_Rear5_df_values = dataframes_list[4]
    #print("Ms22_Rear5_df_values:\n", Ms22_Rear5_df_values)

    Ms22_values = Ms22_Rear5_df_values[0:5]
    #print("Ms22_values_Ms22:\n", Ms22_values)
    Rear5_values = Ms22_Rear5_df_values[5:10]
    #print("Rear5_values_Rear5:\n", Rear5_values)

    Ms22_Rear5_new_df_values = dataframes_list[5]
    print(current_dir)

    #RC1 Model:
    # RC1_df_values = dataframes_list[3]
    # print("C1_df_values:\n", RC1_df_values)

    # RC1_df_values_Ms22 = RC1_df_values[0:5]
    # print("Ms22_values_Ms22:\n", RC1_df_values_Ms22)
    # RC1_df_values_Rear5 = RC1_df_values[5:10]
    # print("Rear5_values_Rear5:\n", RC1_df_values_Rear5)


    #AVG THE VALUES FROM 4 RATS


    w = .9 # bar width
    x = [1, 2, 3, 4, 5, 6] # x-coordinates of your bars
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'black']    # corresponding colors
    y = Ms21_df_values, Ms21_new_df_values, Ms22_Rear5_df_values, Ms22_Rear5_new_df_values, combined_df_values, combined_new_df_values
    #y = [Ms22_values,Rear5_values]
    #y = [nose_values]
 

    fig, ax = plt.subplots()
    ax.bar(x,
           height=[np.mean(yi) for yi in y],
           yerr=[np.std(yi) for yi in y],    # error bars
           capsize=12, # error bar cap width in points
           width=w,    # bar width
           tick_label=["Ms21", "new_Ms21", "Rear5/Ms22", "Rear5/Ms22_new", "combined", "combined_new"],#,"Combined", "RC1"],

           color=(0,0,0,0),  # face color transparent
           edgecolor=colors,
         #ecolor=colors,    # error bar colors; setting this raises an error for whatever reason.
         )

    for i in range(len(x)):
        #distribute scatter randomly across whole width of bar
        a = y[i]
        ax.scatter(x[i] + np.random.random(a[0:5].size) * w - w / 2, a[0:5], color=colors[i], marker='.')
        ax.scatter(x[i] + np.random.random(a[5:10].size) * w - w / 2, a[5:10], color=colors[i], marker = "s")


    # box = ax.get_position()
    # ax.set_position([box.x0, box.y0 + box.height * 0.1,
    #                 box.width, box.height * 0.9])

    # # Put a legend below current axis
    # ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
    #         fancybox=True, shadow=True, ncol=5)

    
    plt.title("Performance of Animal Models")
    plt.xlabel("Animal Model")
    plt.ylabel("% of jumps")
    #plt.legend(['x = x'],bbox_to_anchor =(0.65, 1.25), loc='lower center')
    
    plt.show()
    os.chdir(current_dir + '/saved_figs')
    plt.savefig(fname)


main(pull_path_nose_directory, rump_directory, "rump_results.png")