# Luis Espino 2020

import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Data creation
outlook = [80, 60, 60, 60, 40, 25]
temperature =[0.33, 0.15, 0.15, 0.15, 0.16, 0.4]
humidity = [3.7, 3.7, 3.7, 3.7, 3.7, 3.7]
windy = [35,30,15,15,10,5]

play = [146,209,205,189,213,304]

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

result = clf.predict([[40,0.6,3.7,20]])

# print("labels",l)
print("result",result)
