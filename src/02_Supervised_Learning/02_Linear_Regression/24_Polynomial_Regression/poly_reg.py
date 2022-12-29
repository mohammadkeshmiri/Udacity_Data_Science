# A nice explanation is given here https://data36.com/polynomial-regression-python-scikit-learn/
# TODO: Add import statements
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Change working dir
import os

rootdir = os.path.dirname(os.path.abspath(os.path.basename(__file__)))
print(rootdir)
sys.path.append(rootdir)

from src.utils import change_wd_to_current_file

change_wd_to_current_file()

# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = pd.read_csv('data.csv')
X = train_data['Var_X'].values.reshape(-1,1)
y = train_data['Var_Y'].values

y = [l for _,l in sorted(zip(X,y))]
print(f' X is {X}')
X = np.sort(X, axis=0)
print(f' y is {y}')

# Create polynomial features
# TODO: Create a PolynomialFeatures object, then fit and transform the
# predictor feature
poly_feat = PolynomialFeatures(degree=4)
X_poly = poly_feat.fit_transform(X)

# Make and fit the polynomial regression model
# TODO: Create a LinearRegression object and fit it to the polynomial predictor
# features
poly_model = LinearRegression(fit_intercept = False)
poly_model.fit(X_poly, y)

# Once you've completed all of the steps, select Test Run to see your model
# predictions against the data, or select Submit Answer to check if the degree
# of the polynomial features is the same as ours!

y_predicted = poly_model.predict(X_poly)
# print(y_predicted)

plt.figure()
plt.scatter(X,y)
plt.plot(X, y_predicted, c='red')
plt.show()