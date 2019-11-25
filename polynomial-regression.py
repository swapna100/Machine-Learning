# =================  Polynomial Regression ===================

# Thus far, we have assumed that the relationship between the explanatory
# variables and the response variable is linear. This assumption is not always
# true. This is where polynomial regression comes in. Polynomial regression
# is a special case of multiple linear regression that adds terms with degrees 
# greater than one to the model. The real-world curvilinear relationship is captured
# when you transform the training data by adding polynomial terms, which are then fit in
# the same manner as in multiple linear regression.

# We are now going to us only one explanatory variable, but the model now has
# three terms instead of two. The explanatory variable has been transformed
# and added as a third term to the model to captre the curvilinear relationship.
# The PolynomialFeatures transformer can be used to easily add polynomial features
# to a feature representation. Let's fit a model to these features, and compare it
# to the simple linear regression model:

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Training set
x_train = [[6], [8], [10], [14], [18]] #diamters of pizzas
y_train = [[7], [9], [13], [17.5], [18]] #prices of pizzas

# Testing set
x_test = [[6], [8], [11], [16]] #diamters of pizzas
y_test = [[8], [12], [15], [18]] #prices of pizzas

# Train the Linear Regression model and plot a prediction
regressor = LinearRegression()
regressor.fit(x_train, y_train)
xx = np.linspace(0, 26, 100)
yy = regressor.predict(xx.reshape(xx.shape[0], 1))
plt.plot(xx, yy)

# Set the degree of the Polynomial Regression model
quadratic_featurizer = PolynomialFeatures(degree=2)

# This preprocessor transforms an input data matrix into a new data matrix of a given degree
X_train_quadratic = quadratic_featurizer.fit_transform(x_train)
X_test_quadratic = quadratic_featurizer.transform(x_test)

# Train and test the regressor_quadratic model
regressor_quadratic = LinearRegression()
regressor_quadratic.fit(X_train_quadratic, y_train)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))

# Plot the graph
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), c='r', linestyle='--')
plt.title('Pizza price regressed on diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.scatter(x_train, y_train)
plt.show()
print(x_train)
print (X_train_quadratic)
print (x_test)
print (X_test_quadratic)

# If you execute the code, you will see that the simple linear regression model is plotted with
# a solid line. The quadratic regression model is plotted with a dashed line and evidently
# the quadratic regression model fits the training data better.
