# scikit-learn user guide example

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
# Load the diabetes dataset
# diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X = np.array([100,90,70,40]).reshape(-1,1)
diabetes_y = np.array([45,52,58,62]).reshape(-1,1)

print("diabetes_X",diabetes_X)
print("diabetes_y",diabetes_y)
            
# Use only one feature
# diabetes_X = diabetes_X[:, np.newaxis, 2]

# Split the data into training/testing sets
# diabetes_X_train = diabetes_X[:-20]
# diabetes_X_test = diabetes_X[-20:]

# # Split the targets into training/testing sets
# diabetes_y_train = diabetes_y[:-20]
# diabetes_y_test = diabetes_y[-20:]

# Create linear regression object
regr = PolynomialFeatures(degree=5)

# Train the model using the training sets           
x_pol = regr.fit_transform(diabetes_X)

model = linear_model.LinearRegression()
model.fit(x_pol,diabetes_y)
# Make predictions using the testing set
diabetes_y_pred = model.predict(x_pol)

# The coefficients
rmse = np.sqrt(mean_squared_error(diabetes_y, diabetes_y_pred))
r2 = r2_score(diabetes_y, diabetes_y_pred)
print('RMSE: ', rmse)
print('R2: ', r2)
# Plot outputs
plt.scatter(diabetes_X, diabetes_y,  color='black')
plt.plot(diabetes_X, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

x_new_min = 0.0
x_new_max = 100.0

x_new = np.linspace(x_new_min, x_new_max, 50)
x_new = x_new[:,np.newaxis]

x_new_transform = regr.fit_transform(x_new)
y_new = model.predict(x_new_transform)

print("rmse new", np.sqrt(mean_squared_error(x_new, y_new)))

print("result",y_new)