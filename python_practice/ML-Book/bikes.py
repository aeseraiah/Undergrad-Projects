import csv
from sklearn.ensemble import RandomForestRegressor 
#from housing import plot_feature_importances

def load_dataset(filename):
    file_reader = csv.reader(open(filename, 'rb'), delimiter=',')
    X, y = [], []
    for row in file_reader:
        X.append(row[2:13])
        y.append(row[-1])

    feature_names = np.array(X[0])

    return np.array(X[1:]).astype(np.float32), np.array(y[1:]).astype(np.float32), feature_names

X, y, feature_Names = load_dataset(sys.argv[1])
X, y = shuffle(X, y, random_state=7)

print("X\n",X)
print("y\n",y)
print("feature names\n",feature_name)

#filename = sys.argv[1]


