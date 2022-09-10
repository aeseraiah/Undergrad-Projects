import numpy as np
one_animal_model = np.array([.08, 1, .08, 2.5, 2, 3.7])
analysis_time = one_animal_model[4]

analysis_arr = []
for i in range(1,5):
    analysis_arr.append(analysis_time)

new_arr = []

for i in analysis_arr:
    x = i*1
    new_arr.append(x)
    #print(x)
print(new_arr)