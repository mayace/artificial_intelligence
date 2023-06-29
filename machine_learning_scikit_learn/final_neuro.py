from sklearn.neural_network import MLPClassifier

x = [
    [3.7,35,0.33,80,400,12,], 
    [3.7,30,0.15,60,350,11,], 
    [3.7,15,0.15,60,250,8,], 
    [3.7,15,0.15,60,250,6,], 
    [3.7,10,0.16,40,250,6,], 
    [3.7,5,0.4,25,160,1,], 
     ]
y = [
    [146,250],
    [209,209],
    [205,215],
    [189,252],
    [213,198],
    [304,307],
    ]

model = MLPClassifier(
    activation="logistic",
    random_state=0,
    # max_iter=100,
    # hidden_layer_sizes=(4,),
    # alpha=0.001,
    solver="lbfgs",
)
model.fit(x, y)
print("predictions:", model.predict(x))
