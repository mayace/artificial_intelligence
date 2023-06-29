import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans

x = np.array([
    [3.7,35,0.33,80,400,12,146,250],
    [3.7,30,0.15,60,350,11,209,209],
    [3.7,15,0.15,60,250,8,205,215],
    [3.7,15,0.15,60,250,6,189,252],
    [3.7,10,0.16,40,250,6,213,198],
    [3.7,5,0.4,25,160,1,304,307],
])

kmeans = KMeans(n_clusters=6,max_iter=2000, random_state=0)
kmeans.fit(x)

print(kmeans.cluster_centers_)
print(kmeans.inertia_)

plt.scatter(x[:,0], x[:,1], c=kmeans.labels_, cmap="rainbow")

plt.show()


# for new points
# from sklearn.neighbors import NearestCentroid

# import numpy as np

# X = np.array([
#     [3,2],
#     [5,3],
#     [2,1],
#     [2,2],
#     [6,3],
#     [6,4],
# ])

# Y = np.array(["N","P","N","N","P","P"])
# clf = NearestCentroid()
# clf.fit(X,Y)

# print(clf.predict([[4,4]]))