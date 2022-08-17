import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from pathlib import Path
import numpy as np
import os

#shows 3 graphs in total. First: single, combined. Second: 4 individual trackers. Third: single, avg of 4 ind trackers, combined

full_path_directory = "C:/Users/7teal/Coding Projects/Undergrad-Projects/DeepLabCut/DLC_jump_analysis/all_trackers/"
org_nose_directory = "org_csv_nose_files"
org_rump_directory = "org_csv_rump_files"
nose_directory = "csv_nose_files"
rump_directory = "csv_rump_files"


def main(full_path, relative_path, fname1, fname2):
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

    combined_values = dataframes_list[0]
    print("combined_values:\n", combined_values)
    Ms21_values = dataframes_list[1]
    print("Ms21_values:\n", Ms21_values)
    Ms22_values = dataframes_list[2]
    print("Ms22_values:\n", Ms22_values)
    RC1_values = dataframes_list[3]
    print("RC1_values:\n", RC1_values)
    Rear5_values = dataframes_list[4]
    print("Rear5_values:\n", Rear5_values)
    single_values = dataframes_list[5]
    print("single_values:\n", single_values)

    #Order of single trackers: Ms21, Ms22, RC1, Rear5
    #Naming convention: Ms21 = Rat1, Ms22 = Rat2, RC1 = Rat3, Rear5 = Rat4
  

    w = .9 # bar width
    x1 = [1, 2]
    x2 = [1, 2, 3, 4]
    x3 = [1, 2, 3]
    colors = ['red', 'blue']
    y1 = single_values, combined_values
    y2 = Ms21_values, Ms22_values, RC1_values, Rear5_values 

    labels1 = ['single', 'combined']
    labels2 = ['Ms21', 'Ms22', 'RC1', 'Rear5']
    labels3 = ["single', 'combined', 'individual_avg'"]

    #AVG THE VALUES FROM 3 SINGLE TRACKERS
    avg_per_tracker =[np.mean(yi) for yi in y2]
    print(avg_per_tracker)
    avg_all_trackers = np.mean(avg_per_tracker)
    print("avg_all_trackers:\n", avg_all_trackers)

    y3 = single_values, combined_values, avg_all_trackers


    figure1 = plt.figure(1)
    plt.bar(x1,
           height=[np.mean(yi) for yi in y1],
           yerr=[np.std(yi) for yi in y1],    # error bars
           capsize=12, # error bar cap width in points
           width=w,    # bar width
           tick_label=labels1,
           color=(0,0,0,0),  # face color transparent
           edgecolor=['black'],
        )
    single_combined_bar_val=[np.mean(yi) for yi in y1]
    print("single_combined_bar_val:\n", single_combined_bar_val)

    # exact_values=[np.mean(yi) for yi in y3]
    # print(exact_values)

    # test_a = y1[0] 
    # test_var = np.random.random(test_a[0:5].size)
    # print(test_var)

    for i in range(len(x1)):
        #distribute scatter randomly across whole width of bar
        a = y1[i]
        plt.scatter(x1[i] + np.random.random(a[0:5].size) * w - w / 2, a[0:5], color=colors[1], marker='o') #circle marker = Ms21
        plt.scatter(x1[i] + np.random.random(a[5:10].size) * w - w / 2, a[5:10], color=colors[1], marker = "s") #square marker = Ms22
        plt.scatter(x1[i] + np.random.random(a[10:15].size) * w - w / 2, a[10:15], color=colors[0], marker = "*") #star marker = RC1
        plt.scatter(x1[i] + np.random.random(a[15:20].size) * w - w / 2, a[15:20], color=colors[0], marker = "^") #triangle marker = Rear5

    os.chdir(current_dir + '/saved_figs')
    plt.savefig(fname1, dpi=100)
    plt.show()
    plt.close()


    figure2 = plt.figure(2)
    plt.bar(x2,
           height=[np.mean(yi) for yi in y2],
           yerr=[np.std(yi) for yi in y2],    # error bars
           capsize=12, # error bar cap width in points
           width=w,    # bar width
           tick_label=labels2,
           color=(0,0,0,0),  # face color transparent
           edgecolor=['black'],
         )

    height2=[np.mean(yi) for yi in y2]
    print(height2)
    mean_height = [np.mean(height2)]
    print(mean_height)
    

    #csv order for ind trackers:
    #Ms21: Ms22, RC1, Rear5
    #Ms22: Ms21, RC1, Rear5
    #RC1: Ms21, Ms22, Rear5
    #Rear5: Ms21, Ms22, RC1

    #circle marker = Ms21
    #square marker = Ms22
    #star marker = RC1
    #triangle marker = Rear5


    # Ms21 = y2[0]
    # Ms22 = y2[1]
    # RC1 = y2[2]
    # Rear5 = y2[3]
    # arr_temp = [Ms21, Ms22, RC1, Rear5]

    #for i in range(len(x2)):
    Ms21 = y2[0]
    Ms22 = y2[1]
    RC1 = y2[2]
    Rear5 = y2[3]
    #for i in range(len(arr_temp)):
    #Ms21 Tracker:
    plt.scatter(x2[0] + np.random.random(Ms21[0:5].size) * w - w / 2, Ms21[0:5], color=colors[1], marker='s') #square marker = Ms22
    plt.scatter(x2[0] + np.random.random(Ms21[5:10].size) * w - w / 2, Ms21[5:10], color=colors[0], marker='*') #star marker = RC1
    plt.scatter(x2[0] + np.random.random(Ms21[10:15].size) * w - w / 2, Ms21[10:15], color=colors[0], marker='^') #triangle marker = Rear5

    #Ms22 Tracker:
    plt.scatter(x2[1] + np.random.random(Ms22[0:5].size) * w - w / 2, Ms22[0:5], color=colors[1], marker = "o") #circle marker = Ms21
    plt.scatter(x2[1] + np.random.random(Ms22[5:10].size) * w - w / 2, Ms22[5:10], color=colors[0], marker = "*") #star marker = RC1
    plt.scatter(x2[1] + np.random.random(Ms22[10:15].size) * w - w / 2, Ms22[10:15], color=colors[0], marker='^') #triangle marker = Rear5

    #RC1 Tracker:
    plt.scatter(x2[2] + np.random.random(RC1[0:5].size) * w - w / 2, RC1[0:5], color=colors[1], marker = "o") #circle marker = Ms21
    plt.scatter(x2[2] + np.random.random(RC1[5:10].size) * w - w / 2, RC1[5:10], color=colors[1], marker = "s") #square marker = Ms22
    plt.scatter(x2[2] + np.random.random(RC1[10:15].size) * w - w / 2, RC1[10:15], color=colors[0], marker='^') #triangle marker = Rear5      

    #Rear5 Tracker:
    plt.scatter(x2[3] + np.random.random(Rear5[0:5].size) * w - w / 2, Rear5[0:5], color=colors[1], marker = "o") #circle marker = Ms21
    plt.scatter(x2[3] + np.random.random(Rear5[5:10].size) * w - w / 2, Rear5[5:10], color=colors[1], marker = "s") #square marker = Ms22
    plt.scatter(x2[3] + np.random.random(Rear5[10:15].size) * w - w / 2, Rear5[10:15], color=colors[0], marker='*') #star marker = RC1

  
    plt.savefig(fname2, dpi=100)
    plt.show()
    plt.close()


    #SINGLE, COMBINED, AND AVG GRAPH: 
    # figure3 = plt.figure(1)
    # plt.bar(x3,
    #     height=[np.mean(yi) for yi in y1],
    #     #yerr=[np.std(yi) for yi in y1],    # error bars
    #     capsize=12, # error bar cap width in points
    #     width=w,    # bar width
    #     tick_label=labels3,
    #     color=(0,0,0,0),  # face color transparent
    #     edgecolor=['black'],
    #         )

    # plt.savefig('test_graph.png', dpi=100)
    # plt.show()
    # plt.close()

    
    #LEGEND:
    #box = plt.get_position()
    #plt.set_position([box.x0, box.y0 + box.height * 0.1,
    #                 box.width, box.height * 0.9])
    

    #LEGEND:
    #legend_colors = {'females':'red', 'males':'blue'}
    #labels = list(legend_colors.keys()) 
    #handles = [plt.Rectangle((0,0),1,1, color=legend_colors[labels]) for label in labels]

   
    #ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
    #        fancybox=False, shadow=True, ncol=5)

    # Ms22 = mlines.Line2D([], [], color='blue', marker='.', linestyle='None', markersize=10, label='Ms22')
    # RC1 = mlines.Line2D([], [], color='red', marker='s', linestyle='None', markersize=10, label='RC1')
    # Rear5 = mlines.Line2D([], [], color='red', marker='*', linestyle='None', markersize=10, label='Rear5')
    # Rear1 = mlines.Line2D([], [], color='blue', marker='^', linestyle='None', markersize=10, label='Rear1')
    #female = mlines.Line2D([], [], color='red', marker='^', linestyle='None', markersize=10, label='Rear1')
    #male = mlines.Line2D([], [], color='blue', marker='^', linestyle='None', markersize=10, label='Rear1')
    #female  = mlines.Line2D([], [], marker='hello', linestyle='None', label='female')

    #ax.legend(handles=[Ms22, RC1, Rear5, Rear1, plt.Rectangle((0,0),1,1, color='red'), plt.Rectangle((0,0),1,1, color='blue')])
    #legend = ax.legend(handles=[Ms22, RC1, Rear5, Rear1], (handletextpad=-2.0, handlelength=0))

    # ax.annotate('R: female',xy=(15, -35), xycoords='axes points',
    #         size=10, ha='center', va='bottom',
    #         bbox=dict(boxstyle='square', fc='w'))

    # color_l = ['red', 'blue']
    # for n, text in enumerate(legend.get_texts):
    #     print( n, text)
    #     text.set_color( color_l[n] )

    # plt.title("Performance of Animal Models")
    # plt.xlabel("Animal Model")
    # plt.ylabel("% of jumps")
    # #plt.legend(['x = x'],['s'],bbox_to_anchor =(0.65, 1.25), loc='lower center')


main(full_path_directory, nose_directory, "test-nose-results_single_combined.png", "nose-results_ind.png")#, "nose_results_2.png")