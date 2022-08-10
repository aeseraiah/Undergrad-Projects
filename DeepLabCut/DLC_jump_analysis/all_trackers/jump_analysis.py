import csv
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import os



full_path_directory = "C:/Users/7teal/Coding Projects/Undergrad-Projects/DeepLabCut/DLC_jump_analysis/all_trackers/"
nose_directory = "csv_files"
rump_directory = "csv_rump_files"


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

    combined_new_df_values = dataframes_list[0]
    Ms21_new_df_values = dataframes_list[1]
    #Order of single trackers: Ms22, RC1, Rear5
    Ms22_RC1_Rear5_new_df_values = dataframes_list[2]
    print(Ms22_RC1_Rear5_new_df_values)
    #RC1_new_df_values = dataframes_list[3]
    #AVG THE VALUES FROM 4 RATS
  

    w = .9 # bar width
    x = [1, 2, 3] # x-coordinates of your bars
    colors = ['blue', 'red', 'green']  # corresponding colors
    #y = Ms21_df_values, Ms21_new_df_values, Ms22_Rear5_df_values, Ms22_Rear5_new_df_values, combined_df_values, combined_new_df_values
    y = Ms22_RC1_Rear5_new_df_values, Ms21_new_df_values, combined_new_df_values

    fig, ax = plt.subplots()
    ax.bar(x,
           height=[np.mean(yi) for yi in y],
           yerr=[np.std(yi) for yi in y],    # error bars
           capsize=12, # error bar cap width in points
           width=w,    # bar width
           tick_label=["Rear5/Ms22", "Ms21", "combined"],#"RC1"],
           color=(0,0,0,0),  # face color transparent
           edgecolor=colors,
         #ecolor=colors,    # error bar colors; setting this raises an error for whatever reason.
         )

    for i in range(len(x)):
        #distribute scatter randomly across whole width of bar
        a = y[i]
        ax.scatter(x[i] + np.random.random(a[0:5].size) * w - w / 2, a[0:5], color=colors[i], marker='.')
        ax.scatter(x[i] + np.random.random(a[5:10].size) * w - w / 2, a[5:10], color=colors[i], marker = "s")
        ax.scatter(x[i] + np.random.random(a[5:10].size) * w - w / 2, a[10:15], color=colors[i], marker = "t")

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

    os.chdir(current_dir + '/saved_figs')
    figure = plt.gcf()
    figure.set_size_inches(10, 6)
    plt.savefig(fname, dpi=100)
    plt.show()


main(full_path_directory, nose_directory, "nose_results.png")