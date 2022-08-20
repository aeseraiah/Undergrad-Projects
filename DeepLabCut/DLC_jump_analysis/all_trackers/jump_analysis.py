import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from pathlib import Path
import numpy as np
import os

#shows 3 graphs in total. First: single, combined. Second: 4 individual trackers. Third: single, combined, avg of 4 ind trackers

full_path_directory = "C:/Users/7teal/Coding Projects/Undergrad-Projects/DeepLabCut/DLC_jump_analysis/all_trackers/"
org_nose_directory = "org_csv_nose_files"
org_rump_directory = "org_csv_rump_files"
nose_directory = "csv_nose_files"
rump_directory = "csv_rump_files"


def main(full_path, relative_path, fname1, fname2, fname3):
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
    Ms21_values = dataframes_list[1]
    Ms22_values = dataframes_list[2]
    RC1_values = dataframes_list[3]
    Rear5_values = dataframes_list[4]
    single_values = dataframes_list[5]

    #Order of single trackers: Ms21, Ms22, RC1, Rear5
    #Naming convention: Ms21 = R1, Ms22 = R2, RC1 = R3, Rear5 = R4, R = Rat
  

    w = .9 # bar width
    x1 = [1, 2]
    x2 = [1, 2, 3, 4]
    x3 = [1, 2, 3]
    colors = ['red', 'blue']
    y1 = single_values, combined_values
    y2 = Ms21_values, Ms22_values, RC1_values, Rear5_values

    labels1 = ['Single', 'Combined']
    labels2 = ['Rat 1', 'Rat 2', 'Rat 3', 'Rat 4']
    labels3 = ['Single', 'Combined', 'Individual Model Avg']

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


    for i in range(len(x1)):
        a = y1[i]
        plt.scatter(x1[i] + np.array([0.1, 0.3, 0.5, 0.7, 0.9]) * w - w / 2, a[0:5], color=colors[1], marker='o') #circle marker = Ms21
        plt.scatter(x1[i] + np.array([0.05, 0.25, 0.4, 0.6, 0.8]) * w - w / 2, a[5:10], color=colors[1], marker = "s") #square marker = Ms22
        plt.scatter(x1[i] + np.array([0.15, 0.4, 0.5, 0.7, 0.9]) * w - w / 2, a[10:15], color=colors[0], marker = "*") #star marker = RC1
        plt.scatter(x1[i] + np.array([0.1, 0.4, 0.55, 0.7, 0.9]) * w - w / 2, a[15:20], color=colors[0], marker = "^") #triangle marker = Rear5

    os.chdir(current_dir + '/saved_figs')

    plt.title("Animal Model Performance")
    plt.xlabel("Model")
    plt.ylabel("% of Jumps")

    def legend():
        ax = plt.subplot(111)

        # Shrink current axis by 20%
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        ax.legend(["Rat 1: Male (18-25 months)", "Rat 2: Male (16-20 months)", "Rat 3: Female (10-14 months)", "Rat 4: Female (4-7 months)"], bbox_to_anchor=(1.04, 0.5), loc="best", borderaxespad=0)

    legend()
    plt.savefig(fname1, dpi=200)
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

    ind_tracker_values =[np.mean(yi) for yi in y2]
    ind_trackers_avg = [np.mean(ind_tracker_values)]
    #print("ind_trackers_avg:\n", ind_trackers_avg)

    #csv order for ind trackers:
    #Ms21: Ms22, RC1, Rear5
    #Ms22: Ms21, RC1, Rear5
    #RC1: Ms21, Ms22, Rear5
    #Rear5: Ms21, Ms22, RC1

    #circle marker = Ms21
    #square marker = Ms22
    #star marker = RC1
    #triangle marker = Rear5

    Ms21_tracker = y2[0]
    Ms22_tracker = y2[1]
    RC1_tracker = y2[2]
    Rear5_tracker = y2[3]   


    #Ms21 Tracker:
    plt.scatter(x2[0] + np.array([0.05, 0.25, 0.4, 0.6, 0.8]) * w - w / 2, Ms21_tracker[0:5], color=colors[1], marker='s') #square marker = Ms22
    plt.scatter(x2[0] + np.array([0.12, 0.4, 0.5, 0.7, 0.9]) * w - w / 2, Ms21_tracker[5:10], color=colors[0], marker='*') #star marker = RC1
    plt.scatter(x2[0] + np.array([0.1, 0.4, 0.55, 0.7, 0.9]) * w - w / 2, Ms21_tracker[10:15], color=colors[0], marker='^') #triangle marker = Rear5

    #Ms22 Tracker:
    plt.scatter(x2[1] + np.array([0.8, 0.3, 0.5, 0.7, 0.9]) * w - w / 2, Ms22_tracker[0:5], color=colors[1], marker = "o") #circle marker = Ms21
    plt.scatter(x2[1] + np.array([0.12, 0.4, 0.5, 0.7, 0.9]) * w - w / 2, Ms22_tracker[5:10], color=colors[0], marker = "*") #star marker = RC1
    plt.scatter(x2[1] + np.array([0.1, 0.4, 0.55, 0.7, 0.9]) * w - w / 2, Ms22_tracker[10:15], color=colors[0], marker='^') #triangle marker = Rear5

    #RC1 Tracker:
    plt.scatter(x2[2] + np.array([0.8, 0.3, 0.5, 0.7, 0.9]) * w - w / 2, RC1_tracker[0:5], color=colors[1], marker = "o") #circle marker = Ms21
    plt.scatter(x2[2] + np.array([0.05, 0.25, 0.4, 0.6, 0.8]) * w - w / 2, RC1_tracker[5:10], color=colors[1], marker = "s") #square marker = Ms22
    plt.scatter(x2[2] + np.array([0.1, 0.4, 0.55, 0.7, 0.9]) * w - w / 2, RC1_tracker[10:15], color=colors[0], marker='^') #triangle marker = Rear5      

    #Rear5 Tracker:
    plt.scatter(x2[3] + np.array([0.8, 0.3, 0.5, 0.7, 0.9]) * w - w / 2, Rear5_tracker[0:5], color=colors[1], marker = "o") #circle marker = Ms21
    plt.scatter(x2[3] + np.array([0.05, 0.25, 0.4, 0.6, 0.8]) * w - w / 2, Rear5_tracker[5:10], color=colors[1], marker = "s") #square marker = Ms22
    plt.scatter(x2[3] + np.array([0.12, 0.4, 0.5, 0.7, 0.9]) * w - w / 2, Rear5_tracker[10:15], color=colors[0], marker='*') #star marker = RC1

  
    plt.title("Animal Model Performance")
    plt.xlabel("Individual Model")
    plt.ylabel("% of Jumps")

    legend()
    plt.savefig(fname2, dpi=100)
    plt.show()
    plt.close()


    #FINDING AVERAGES OF 5 VIDEOS (FROM EACH ANIMAL) ANALYZED WITH ALL 4 INDIVIDUAL TRACKERS:

    #MS21 VIDEOS:
    Ms21_first_vid = (np.mean(Ms22_tracker[0]) + np.mean(RC1_tracker[0]) + np.mean(Rear5_tracker[0])) / 3
    Ms21_second_vid = (np.mean(Ms22_tracker[1]) + np.mean(RC1_tracker[1]) + np.mean(Rear5_tracker[1])) / 3
    Ms21_third_vid = (np.mean(Ms22_tracker[2]) + np.mean(RC1_tracker[2]) + np.mean(Rear5_tracker[2])) / 3
    Ms21_fourth_vid = (np.mean(Ms22_tracker[3]) + np.mean(RC1_tracker[3]) + np.mean(Rear5_tracker[3])) / 3
    Ms21_fifth_vid = (np.mean(Ms22_tracker[4]) + np.mean(RC1_tracker[4]) + np.mean(Rear5_tracker[4])) / 3

    Ms21_avg_five_vids = [Ms21_first_vid,  Ms21_second_vid, Ms21_third_vid, Ms21_fourth_vid, Ms21_fifth_vid]
    #print("Ms21_avg_five_vids:\n", Ms21_avg_five_vids)


    #MS22 VIDEOS:
    Ms22_first_vid = (np.mean(Ms21_tracker[0]) + np.mean(RC1_tracker[6]) + np.mean(Rear5_tracker[6])) / 3
    Ms22_second_vid = (np.mean(Ms21_tracker[1]) + np.mean(RC1_tracker[7]) + np.mean(Rear5_tracker[7])) / 3
    Ms22_third_vid = (np.mean(Ms21_tracker[2]) + np.mean(RC1_tracker[8]) + np.mean(Rear5_tracker[8])) / 3
    Ms22_fourth_vid = (np.mean(Ms21_tracker[3]) + np.mean(RC1_tracker[9]) + np.mean(Rear5_tracker[9])) / 3
    Ms22_fifth_vid = (np.mean(Ms21_tracker[4]) + np.mean(RC1_tracker[10]) + np.mean(Rear5_tracker[10])) / 3

    Ms22_avg_five_vids = [Ms22_first_vid,  Ms22_second_vid, Ms22_third_vid, Ms22_fourth_vid, Ms22_fifth_vid]
    #print("Ms22_avg_five_vids:\n", Ms22_avg_five_vids)

    #RC1 VIDEOS:
    RC1_first_vid = (np.mean(Ms21_tracker[6]) + np.mean(Ms22_tracker[6]) + np.mean(Rear5_tracker[10])) / 3
    RC1_second_vid = (np.mean(Ms21_tracker[7]) + np.mean(Ms22_tracker[7]) + np.mean(Rear5_tracker[11])) / 3
    RC1_third_vid = (np.mean(Ms21_tracker[8]) + np.mean(Ms22_tracker[8]) + np.mean(Rear5_tracker[12])) / 3
    RC1_fourth_vid = (np.mean(Ms21_tracker[9]) + np.mean(Ms22_tracker[9]) + np.mean(Rear5_tracker[13])) / 3
    RC1_fifth_vid = (np.mean(Ms21_tracker[10]) + np.mean(Ms22_tracker[10]) + np.mean(Rear5_tracker[14])) / 3

    RC1_avg_five_vids = [RC1_first_vid,  RC1_second_vid, RC1_third_vid, RC1_fourth_vid, RC1_fifth_vid]
    #print("RC1_avg_five_vids:\n", RC1_avg_five_vids)

    #REAR5 VIDEOS:
    Rear5_first_vid = (np.mean(Ms21_tracker[10]) + np.mean(Ms22_tracker[10]) + np.mean(RC1_tracker[10])) / 3
    Rear5_second_vid = (np.mean(Ms21_tracker[11]) + np.mean(Ms22_tracker[11]) + np.mean(RC1_tracker[11])) / 3
    Rear5_third_vid = (np.mean(Ms21_tracker[12]) + np.mean(Ms22_tracker[12]) + np.mean(RC1_tracker[12])) / 3
    Rear5_fourth_vid = (np.mean(Ms21_tracker[13]) + np.mean(Ms22_tracker[13]) + np.mean(RC1_tracker[13])) / 3
    Rear5_fifth_vid = (np.mean(Ms21_tracker[14]) + np.mean(Ms22_tracker[14]) + np.mean(RC1_tracker[14])) / 3

    Rear5_avg_five_vids = [Rear5_first_vid,  Rear5_second_vid, Rear5_third_vid, Rear5_fourth_vid, Rear5_fifth_vid]
    #print("Rear5_avg_five_vids:\n", Rear5_avg_five_vids)

    final_avg_ind_trackers = np.concatenate((Ms21_avg_five_vids, Ms22_avg_five_vids, RC1_avg_five_vids, Rear5_avg_five_vids))
    #print("final_avg_ind_trackers:\n", final_avg_ind_trackers)



    #SINGLE, COMBINED, AND AVG GRAPH:
    y3 = single_values, combined_values, final_avg_ind_trackers
    figure3 = plt.figure(3)
    plt.bar(x3,
        height=[np.mean(yi) for yi in y3],
        yerr=[np.std(yi) for yi in y3],    # error bars
        capsize=12, # error bar cap width in points
        width=w,    # bar width
        tick_label=labels3,
        color=(0,0,0,0),  # face color transparent
        edgecolor=['black'],
            )

    all_bar_val =[np.mean(final_avg_ind_trackers)]
    print("\nfinal_avg_ind_trackers:\n", all_bar_val)

    #Aligning videos analyzed on each tracker:
    # arr = np.random.RandomState(1111)
    # xb = arr.uniform(0,.95,5)
    # array = np.array(xb)
    # array2 = np.sort(array)
    # print(array2)
   
    for i in range(len(x3)):
        a = y3[i]
        plt.scatter(x3[i] + np.array([0.1, 0.3, 0.5, 0.7, 0.9]) * w - w / 2, a[0:5], color=colors[1], marker='o') #circle marker = Ms21
        plt.scatter(x3[i] + np.array([0.05, 0.25, 0.4, 0.6, 0.8]) * w - w / 2, a[5:10], color=colors[1], marker = "s") #square marker = Ms22
        plt.scatter(x3[i] + np.array([0.15, 0.4, 0.6, 0.7, 0.9]) * w - w / 2, a[10:15], color=colors[0], marker = "*") #star marker = RC1
        plt.scatter(x3[i] + np.array([0.1, 0.4, 0.55, 0.7, 0.9]) * w - w / 2, a[15:20], color=colors[0], marker = "^") #triangle marker = Rear5

    plt.title("Animal Model Performance")
    plt.xlabel("Model")
    plt.ylabel("% of Jumps")
       
    legend()
    plt.savefig(fname3, dpi=200)
    plt.show()
    plt.close()

main(full_path_directory, nose_directory, "test-nose-results_single_combined.png", "nose-results_ind.png", "nose-results-all.png")#, "nose_results_2.png")