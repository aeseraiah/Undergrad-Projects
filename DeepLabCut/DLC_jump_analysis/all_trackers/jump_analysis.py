import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
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
    #Ms22_new_df_values = dataframes_list[1]
    #RC1_new_df_values = dataframes_list[2]
    #Rear5_new_df_values = dataframes_list[3]
    single_trackers_df = dataframes_list[2]
    #Order of single trackers: Ms22, RC1, Rear5

    #AVG THE VALUES FROM 3 SINGLE TRACKERS
    #avg_new_df_values = 
  

    w = .9 # bar width
    x = [1, 2]
    colors = ['red','blue']
    #y = Ms22_new_df_values, RC1_new_df_values, Rear5_new_df_values
    #y = single_trackers_df, combined_new_df_values, avg_new_df_values
    y = single_trackers_df, combined_new_df_values

    fig, ax = plt.subplots()
    ax.bar(x,
           height=[np.mean(yi) for yi in y],
           yerr=[np.std(yi) for yi in y],    # error bars
           capsize=12, # error bar cap width in points
           width=w,    # bar width
           #tick_label=["Rear5/Ms22", "Ms22", "combined"],#"RC1"],
           tick_label=['single trackers', 'combined tracker'],
           color=(0,0,0,0),  # face color transparent
           edgecolor=['black'],
         #ecolor=colors,    # error bar colors; setting this raises an error for whatever reason.
         )


    for i in range(len(x)):
        #distribute scatter randomly across whole width of bar
        a = y[i]
        #print(y)
        ax.scatter(x[i] + np.random.random(a[0:5].size) * w - w / 2, a[0:5], color=colors[1], marker='.') #circle marker = Ms22
        ax.scatter(x[i] + np.random.random(a[5:10].size) * w - w / 2, a[5:10], color=colors[0], marker = "s") #square marker = RC1
        ax.scatter(x[i] + np.random.random(a[10:15].size) * w - w / 2, a[10:15], color=colors[0], marker = "*") #star marker = Rear5

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])
    

    # # Put a legend below current axis
    #legend_colors = {'females':'red', 'males':'blue'}
    #labels = list(legend_colors.keys()) 
    #handles = [plt.Rectangle((0,0),1,1, color=legend_colors[labels]) for label in labels]

   
    #ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
    #        fancybox=False, shadow=True, ncol=5)

    Ms22 = mlines.Line2D([], [], color='blue', marker='.', linestyle='None', markersize=10, label='Ms22')
    RC1 = mlines.Line2D([], [], color='red', marker='s', linestyle='None', markersize=10, label='RC1')
    Rear5 = mlines.Line2D([], [], color='red', marker='*', linestyle='None', markersize=10, label='Rear5')
    Rear1 = mlines.Line2D([], [], color='blue', marker='^', linestyle='None', markersize=10, label='Rear1')
    #female = mlines.Line2D([], [], color='red', marker='^', linestyle='None', markersize=10, label='Rear1')
    #male = mlines.Line2D([], [], color='blue', marker='^', linestyle='None', markersize=10, label='Rear1')
    #female  = mlines.Line2D([], [], marker='hello', linestyle='None', label='female')

    #ax.legend(handles=[Ms22, RC1, Rear5, Rear1, plt.Rectangle((0,0),1,1, color='red'), plt.Rectangle((0,0),1,1, color='blue')])
    legend = ax.legend(handles=[Ms22, RC1, Rear5, Rear1], (handletextpad=-2.0, handlelength=0))

    # ax.annotate('R: female',xy=(15, -35), xycoords='axes points',
    #         size=10, ha='center', va='bottom',
    #         bbox=dict(boxstyle='square', fc='w'))

    color_l = ['red', 'blue']
    for n, text in enumerate(legend.get_texts):
        print( n, text)
        text.set_color( color_l[n] )

    plt.title("Performance of Animal Models")
    plt.xlabel("Animal Model")
    plt.ylabel("% of jumps")
    #plt.legend(['x = x'],['s'],bbox_to_anchor =(0.65, 1.25), loc='lower center')

    os.chdir(current_dir + '/saved_figs')
    figure = plt.gcf()
    figure.set_size_inches(10, 6)
    plt.savefig(fname, dpi=100)
    plt.show()


main(full_path_directory, nose_directory, "nose_results.png")