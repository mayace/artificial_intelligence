# Luis Espino 2020

import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Data creation
outlook=[
    10.5,
9.8,
11.2,
9.2,
9.1,
10.8,
11.5,
11.2,
10.3,
9.7,
]
temperature=[
    1,
5,
20,
60,
90,
120,
180,
220,
340,
410,
]
humidity=[
    400.5,
405.8,
410.9,
425.4,
450.1,
500.5,
575.7,
456.5,
320.1,
221.9,
]
windy=[1,
0,
0,
0,
1,
1,
0,
1,
0,
0,]
play=[
    0,
1,
1,
0,
1,
1,
0,
1,
0,
1,
]

# Import LabelEncoder
from sklearn import preprocessing

# Creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
outlook_encoded=outlook
temperature_encoded=temperature
humidity_encoded=humidity
windy_encoded=windy
label=play

print ("outlook:  ",outlook_encoded)
print ("temp:     ",temperature_encoded)
print ("humidity: ",humidity_encoded)
print ("windy:    ",windy_encoded)
print ("PLAY:     ",label)

# Combinig attributes into single listof tuples
features=list(zip(outlook_encoded,temperature_encoded,humidity_encoded,windy_encoded))
print (features)

# fit the model
clf = DecisionTreeClassifier().fit(features, label)
plot_tree(clf, filled=True)
plt.show()


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(features,label)
predicted = model.predict([[100,0,100,0]])
print("predicted:", predicted)
