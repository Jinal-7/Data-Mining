from sklearn import svm
from sklearn.svm import SVR
import copy

data = [[1,1,1,0,0,0,1,0],
        [0,1,0,0,1,1,0,1],
        [1,0,0,1,0,0,0,1],
        [1,1,0,0,1,0,0,0],
        [1,0,1,1,0,0,1,0],
        [0,1,1,0,0,0,0,1],
        [0,0,0,0,1,1,1,1],
        [1,0,0,1,1,1,0,0],
        [1,0,0,0,1,0,0,1],
        [0,1,0,1,0,0,1,1]]

pred = copy.deepcopy(data)
n_users = len(pred)
n_movies = len(pred[0])

for u in range(n_users):
    for m in range(n_movies):
        if pred[u][m] == 0:
            Y = []
            X = []
            for i in range(n_users):
                if (i == u):
                    continue
                X.append(data[i][:m] + data[i][m + 1:])
                Y.append(data[i][m])
                clf = SVR(C=1.0, epsilon=0.2)
                c = clf.fit(X, Y)
                val = clf.predict([data[u][:m] + data[u][m + 1:]])
                pred[u][m] = round(val[0], 2)

for vals in pred:
   print(vals)