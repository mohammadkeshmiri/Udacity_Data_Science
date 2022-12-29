# TODO: Add import statements
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
import sys
import os

rootdir = os.path.dirname(os.path.abspath(os.path.basename(__file__)))
print(rootdir)
sys.path.append(rootdir)

from src.utils import change_wd_to_current_file

change_wd_to_current_file()

# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = pd.read_csv('data.csv', header=None)
print(train_data)
X = train_data.iloc[:,:-1]
y = train_data.iloc[:,-1]

# TODO: Create the linear regression model with lasso regularization.
lasso_reg = Lasso()
lg = LinearRegression()

# TODO: Fit the model.
lasso_reg.fit(X,y)
lg.fit(X,y)


# TODO: Retrieve and print out the coefficients from the regression model.
reg_coef = lasso_reg.coef_
print(reg_coef)
print(lg.coef_)