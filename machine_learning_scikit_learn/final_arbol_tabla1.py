# Luis Espino 2020

import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Data creation
outlook = [3.7, 3.7, 3.7, 3.7, 3.7, 3.7]
temperature = [0.33, 0.15, 0.15, 0.15, 0.16, 0.4]
humidity = [80, 60, 60, 60, 40, 25]
windy = [4000, 3500, 2500, 2500, 2500, 1600]

play = [250, 209, 215, 252, 198, 307]

# Import LabelEncoder
from sklearn import preprocessing

# Creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
outlook_encoded = outlook
temperature_encoded = temperature
humidity_encoded = humidity
windy_encoded = windy
label = play

print("outlook:  ", outlook_encoded)
print("temp:     ", temperature_encoded)
print("humidity: ", humidity_encoded)
print("windy:    ", windy_encoded)
print("PLAY:     ", label)

# Combinig attributes into single listof tuples
features = list(
    zip(outlook_encoded, temperature_encoded, humidity_encoded, windy_encoded)
)
print(features)

# fit the model
clf = DecisionTreeClassifier(
    criterion="entropy", random_state=0, splitter="random"
).fit(features, label)
plot_tree(clf, filled=True)
plt.show()

# result = clf.predict([[3.7,0.6,40,2000]])
result = clf.predict([[3.7,0.15,75,4000]])

print("result",result)
