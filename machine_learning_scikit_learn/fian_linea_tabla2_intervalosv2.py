# scikit-learn user guide example

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
# diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X = [[40],[30],[30],[10]]
diabetes_y = [62,58,52,45]

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
regr = linear_model.LinearRegression()

# Train the model using the training sets           
regr.fit(diabetes_X, diabetes_y)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(diabetes_y, diabetes_y_pred,squared=False))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(diabetes_y, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X, diabetes_y,  color='black')
plt.plot(diabetes_X, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

result = regr.predict([[95]])

print("result",result)