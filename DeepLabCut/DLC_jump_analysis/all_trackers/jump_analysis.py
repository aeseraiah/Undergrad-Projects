import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#shows 3 graphs in total. First: single, combined. Second: 4 individual trackers. Third: single, combined, avg of 4 ind trackers

org_nose_directory = "org_csv_nose_files"
org_rump_directory = "org_csv_rump_files"
nose_directory = "csv_nose_files"
rump_directory = "csv_rump_files"

full_path_directory = os.getcwd()
# nose_path = full_path_directory + '/' + nose_directory
# rump_path = full_path_directory + '/' + nose_directory

# is_noseDir= os.path.isdir(nose_path)
# print(is_noseDir)

# is_rumpDir= os.path.isdir(rump_path)
# print(is_rumpDir)

# if is_noseDir == False:
#     os.mkdir(nose_path)
# if is_rumpDir == False:
#     os.mkdir(rump_path)

def main(full_path, relative_path, fname1, fname2, fname3):
    current_dir = os.getcwd()
    os.chdir(current_dir + '/' + relative_path)

    
    for root, dirs, files in os.walk(".", topdown=False):
        #for name in files:
        #    print(os.path.join(root, name))
        file_count = len(files)


    jump_values = []
    for i in range(file_count):
        read_csv = pd.read_csv(files[i])
        all_dataframes = pd.DataFrame(read_csv)
        column_values = all_dataframes.columns.values.astype(float)
        jump_values.append(column_values)

    combined_values = jump_values[0]
    Ms21_values = jump_values[1]
    Ms22_values = jump_values[2]
    RC1_values = jump_values[3]
    Rear5_values = jump_values[4]
    single_values = jump_values[5]

    #Order of single trackers: Ms21, Ms22, RC1, Rear5
    #Naming convention: Ms21 = Rat1 1, Ms22 = Rat 2 , RC1 = Rat 3, Rear5 = Rat 4
  

    w = .9
    x_fig1 = [1, 2]
    x_fig2 = [1, 2, 3, 4]
    x_fig3 = [1, 2, 3]
    y_fig1 = single_values, combined_values
    y_fig2 = Ms21_values, Ms22_values, RC1_values, Rear5_values
    colors = ['red', 'blue'] #female or male 

    labels_fig1 = ['Single', 'Combined']
    labels_fig2 = ['Rat 1', 'Rat 2', 'Rat 3', 'Rat 4']
    labels_fig3 = ['Single', 'Combined', 'Ind Avg']

    plt.rcParams["figure.figsize"] = (13,6)
    figure1 = plt.figure(1)
    plt.bar(x_fig1,
           height=[np.mean(yi) for yi in y_fig1],
           yerr=[np.std(yi) for yi in y_fig1], # error bars
           capsize=12, # error bar cap width in points
           width=w, # bar width
           tick_label=labels_fig1,
           color=(0,0,0,0), # face color transparent
           edgecolor=['black'],
        )
    single_combined_avgs=[np.mean(yi) for yi in y_fig1]
    print("single and combined avgs:\n", single_combined_avgs)


    for i in range(len(x_fig1)):
        y = y_fig1[i]
        plt.scatter(x_fig1[i] + np.array([0.1, 0.3, 0.5, 0.7, 0.9]) * w - w / 2, y[0:5], color=colors[1], marker='.') #circle marker = Ms21
        plt.scatter(x_fig1[i] + np.array([0.05, 0.25, 0.4, 0.6, 0.8]) * w - w / 2, y[5:10], color=colors[1], marker = "s") #square marker = Ms22
        plt.scatter(x_fig1[i] + np.array([0.15, 0.4, 0.5, 0.7, 0.9]) * w - w / 2, y[10:15], color=colors[0], marker = "*") #star marker = RC1
        plt.scatter(x_fig1[i] + np.array([0.1, 0.4, 0.55, 0.7, 0.9]) * w - w / 2, y[15:20], color=colors[0], marker = "^") #triangle marker = Rear5

    os.chdir(current_dir + '/saved_figs')


    plt.ylim(0, 30)
    plt.title("Animal Model Performance")
    plt.xlabel("Model")
    plt.ylabel("% of Jumps")

    def legend():
        ax = plt.subplot(111)

        # Shrink current axis by 20%
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        ax.legend(["Rat 1: Male, 18-25 months", "Rat 2: Male, 16-20 months", "Rat 3: Female, 10-14 months", "Rat 4: Female, 4-7 months"], bbox_to_anchor=(1.04, 1), borderaxespad=0)

    #legend()
    plt.savefig(fname1, dpi=200)
    plt.show()
    plt.close()

    plt.rcParams["figure.figsize"] = (13,6)
    figure2 = plt.figure(2)
    plt.bar(x_fig2,
           height=[np.mean(yi) for yi in y_fig2],
           yerr=[np.std(yi) for yi in y_fig2], # error bars
           capsize=12, # error bar cap width in points
           width=w, # bar width
           tick_label=labels_fig2,
           color=(0,0,0,0), # face color transparent
           edgecolor=['black'],
         )

    ind_tracker_avgs =[np.mean(yi) for yi in y_fig2]
    ind_trackers_one_avg = [(ind_tracker_avgs)]
    print("\nind trackers avgs:\n", ind_tracker_avgs)

    #csv order for ind trackers:
    #Ms21: Ms22, RC1, Rear5
    #Ms22: Ms21, RC1, Rear5
    #RC1: Ms21, Ms22, Rear5
    #Rear5: Ms21, Ms22, RC1

    #Marker for Individual Rats: 
    #circle marker = Ms21
    #square marker = Ms22
    #star marker = RC1
    #triangle marker = Rear5

    Ms21_tracker = y_fig2[0]
    Ms22_tracker = y_fig2[1]
    RC1_tracker = y_fig2[2]
    Rear5_tracker = y_fig2[3]   


    #Ms21 Tracker:
    plt.scatter(x_fig2[0] + np.array([0.05, 0.25, 0.4, 0.6, 0.8]) * w - w / 2, Ms21_tracker[0:5], color=colors[1], marker='s') #square marker = Ms22
    plt.scatter(x_fig2[0] + np.array([0.12, 0.4, 0.5, 0.7, 0.9]) * w - w / 2, Ms21_tracker[5:10], color=colors[0], marker='*') #star marker = RC1
    plt.scatter(x_fig2[0] + np.array([0.1, 0.4, 0.55, 0.7, 0.9]) * w - w / 2, Ms21_tracker[10:15], color=colors[0], marker='^') #triangle marker = Rear5

    #Ms22 Tracker:
    plt.scatter(x_fig2[1] + np.array([0.08, 0.3, 0.5, 0.7, 0.9]) * w - w / 2, Ms22_tracker[0:5], color=colors[1], marker = ".") #circle marker = Ms21
    plt.scatter(x_fig2[1] + np.array([0.2, 0.4, 0.5, 0.7, 0.9]) * w - w / 2, Ms22_tracker[5:10], color=colors[0], marker = "*") #star marker = RC1
    plt.scatter(x_fig2[1] + np.array([0.1, 0.4, 0.55, 0.7, 0.9]) * w - w / 2, Ms22_tracker[10:15], color=colors[0], marker='^') #triangle marker = Rear5

    #RC1 Tracker:
    plt.scatter(x_fig2[2] + np.array([0.1, 0.3, 0.5, 0.7, 0.9]) * w - w / 2, RC1_tracker[0:5], color=colors[1], marker = ".") #circle marker = Ms21
    plt.scatter(x_fig2[2] + np.array([0.05, 0.25, 0.4, 0.6, 0.8]) * w - w / 2, RC1_tracker[5:10], color=colors[1], marker = "s") #square marker = Ms22
    plt.scatter(x_fig2[2] + np.array([0.1, 0.4, 0.55, 0.7, 0.9]) * w - w / 2, RC1_tracker[10:15], color=colors[0], marker='^') #triangle marker = Rear5      

    #Rear5 Tracker:
    #made changes to first line: .7, .9
    plt.scatter(x_fig2[3] + np.array([0.08, 0.3, 0.5, 0.8, 0.95]) * w - w / 2, Rear5_tracker[0:5], color=colors[1], marker = ".") #circle marker = Ms21
    plt.scatter(x_fig2[3] + np.array([0.05, 0.25, 0.4, 0.6, 0.8]) * w - w / 2, Rear5_tracker[5:10], color=colors[1], marker = "s") #square marker = Ms22
    plt.scatter(x_fig2[3] + np.array([0.12, 0.4, 0.5, 0.7, 0.9]) * w - w / 2, Rear5_tracker[10:15], color=colors[0], marker='*') #star marker = RC1

  
    plt.ylim(0, 30)
    plt.title("Animal Model Performance")
    plt.xlabel("Individual Model")
    plt.ylabel("% of Jumps")
    #legend()
    plt.savefig(fname2, dpi=100)
    plt.show()
    plt.close()


    #FINDING AVERAGES OF 5 VIDEOS (FROM EACH ANIMAL) ANALYZED WITH ALL 4 INDIVIDUAL TRACKERS:

    #MS21 VIDEOS:
    Ms21_first_vid = np.mean([(Ms22_tracker[0]), (RC1_tracker[0]), (Rear5_tracker[0])])
    Ms21_second_vid = np.mean([(Ms22_tracker[1]), (RC1_tracker[1]), (Rear5_tracker[1])])
    Ms21_third_vid = np.mean([(Ms22_tracker[2]), (RC1_tracker[2]), (Rear5_tracker[2])])
    Ms21_fourth_vid = np.mean([(Ms22_tracker[3]), (RC1_tracker[3]), (Rear5_tracker[3])])
    Ms21_fifth_vid = np.mean([(Ms22_tracker[4]), (RC1_tracker[4]), (Rear5_tracker[4])])

    Ms21_avg_five_vids = [Ms21_first_vid,  Ms21_second_vid, Ms21_third_vid, Ms21_fourth_vid, Ms21_fifth_vid]


    #MS22 VIDEOS:
    Ms22_first_vid = np.mean([(Ms21_tracker[0]), (RC1_tracker[6]), (Rear5_tracker[6])])
    Ms22_second_vid = np.mean([(Ms21_tracker[1]), (RC1_tracker[7]), (Rear5_tracker[7])])
    Ms22_third_vid = np.mean([(Ms21_tracker[2]), (RC1_tracker[8]), (Rear5_tracker[8])])
    Ms22_fourth_vid = np.mean([(Ms21_tracker[3]), (RC1_tracker[9]), (Rear5_tracker[9])])
    Ms22_fifth_vid = np.mean([(Ms21_tracker[4]), (RC1_tracker[10]), (Rear5_tracker[10])])

    Ms22_avg_five_vids = [Ms22_first_vid,  Ms22_second_vid, Ms22_third_vid, Ms22_fourth_vid, Ms22_fifth_vid]

    #RC1 VIDEOS:
    RC1_first_vid = np.mean([(Ms21_tracker[6]), (Ms22_tracker[6]), (Rear5_tracker[10])])
    RC1_second_vid = np.mean([(Ms21_tracker[7]), (Ms22_tracker[7]), (Rear5_tracker[11])])
    RC1_third_vid = np.mean([(Ms21_tracker[8]), (Ms22_tracker[8]), (Rear5_tracker[12])])
    RC1_fourth_vid = np.mean([(Ms21_tracker[9]), (Ms22_tracker[9]), (Rear5_tracker[13])])
    RC1_fifth_vid = np.mean([(Ms21_tracker[10]), (Ms22_tracker[10]), (Rear5_tracker[14])])

    RC1_avg_five_vids = [RC1_first_vid,  RC1_second_vid, RC1_third_vid, RC1_fourth_vid, RC1_fifth_vid]


    #REAR5 VIDEOS:
    Rear5_first_vid = np.mean([(Ms21_tracker[10]), (Ms22_tracker[10]), (RC1_tracker[10])])
    Rear5_second_vid = np.mean([(Ms21_tracker[11]), (Ms22_tracker[11]), (RC1_tracker[11])])
    Rear5_third_vid = np.mean([(Ms21_tracker[12]), (Ms22_tracker[12]), (RC1_tracker[12])])
    Rear5_fourth_vid = np.mean([(Ms21_tracker[13]), (Ms22_tracker[13]), (RC1_tracker[13])])
    Rear5_fifth_vid = np.mean([(Ms21_tracker[14]), (Ms22_tracker[14]), (RC1_tracker[14])])

    Rear5_avg_five_vids = [Rear5_first_vid,  Rear5_second_vid, Rear5_third_vid, Rear5_fourth_vid, Rear5_fifth_vid]


    final_avg_ind_trackers = np.concatenate((Ms21_avg_five_vids, Ms22_avg_five_vids, RC1_avg_five_vids, Rear5_avg_five_vids))




    #SINGLE, COMBINED, AND AVG GRAPH:
    y_fig3 = single_values, combined_values, final_avg_ind_trackers
    plt.rcParams["figure.figsize"] = (13,6)

    figure3 = plt.figure(3)
    plt.bar(x_fig3,
        height=[np.mean(yi) for yi in y_fig3],
        yerr=[np.std(yi) for yi in y_fig3],    # error bars
        capsize=12, # error bar cap width in points
        width=w,    # bar width
        tick_label=labels_fig3,
        color=(0,0,0,0),  # face color transparent
        edgecolor=['black'],
        zorder=1
            )

    all_bar_val =[np.mean(final_avg_ind_trackers)]
    print("\nind trackers combined avg\n", all_bar_val)

    #Aligning videos analyzed on each tracker:
    # arr = np.random.RandomState(1111)
    # xb = arr.uniform(0,.95,5)
    # array = np.array(xb)
    # array_fig2 = np.sort(array)
    # print(array_fig2)
   
    for i in range(len(x_fig3)):
        y = y_fig3[i]
        plt.scatter(x_fig3[i] + np.array([0.1, 0.3, 0.5, 0.7, 0.9]) * w - w / 2, y[0:5], color=colors[1], marker='.') #circle marker = Ms21
        plt.scatter(x_fig3[i] + np.array([0.05, 0.25, 0.4, 0.6, 0.8]) * w - w / 2, y[5:10], color=colors[1], marker = "s") #square marker = Ms22
        plt.scatter(x_fig3[i] + np.array([0.15, 0.4, 0.6, 0.7, 0.9]) * w - w / 2, y[10:15], color=colors[0], marker = "*") #star marker = RC1
        plt.scatter(x_fig3[i] + np.array([0.1, 0.4, 0.55, 0.7, 0.9]) * w - w / 2, y[15:20], color=colors[0], marker = "^") #triangle marker = Rear5


    plt.grid(color='grey', linestyle='-', linewidth=.1, axis='y')
    plt.ylim(0, 30)
    plt.title("Animal Model Performance")
    plt.xlabel("Model")
    plt.ylabel("% of Jumps")
    #legend()
    plt.savefig(fname3, dpi=200)
    plt.show()
    plt.close()

    #print(single_values, combined_values)


main(full_path_directory, nose_directory, "nose_jumps_single_combined.png", "nose_jumps_inds.png", "nose_jumps_ind-avg.png")
#main(full_path_directory, rump_directory, "rump_jumps_single_combined.png", "rump_jumps_inds.png", "rump_jumps_ind-avg.png")