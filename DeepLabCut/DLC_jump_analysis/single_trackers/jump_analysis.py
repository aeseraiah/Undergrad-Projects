import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def main():
    # for i in nose_csv_list:
    #     nose = pd.read_csv(i)
    #     nose_df = pd.DataFrame(nose)
    #     nose_values = nose_df.columns.values.astype(float)

    nose_directory = 'csv_files'
    #NOTE: change nose_directory in for loop to rump_directory to make the other bar graph
    rump_directory = 'csv_rump_files'
    
    # iterate over files in
    # that directory
    arr = []
    for filename in os.listdir(nose_directory):
        f = os.path.join(nose_directory, filename)
        print(filename)
        nose = pd.read_csv(filename)
        nose_df = pd.DataFrame(nose)
        nose_values = nose_df.columns.values.astype(float)
        #print(nose_values)
        # for i in nose_values:
        #     arr[i] = nose_values
    #print(arr)





main()



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