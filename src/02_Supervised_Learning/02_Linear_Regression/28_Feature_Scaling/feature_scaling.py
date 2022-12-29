# TODO: Add import statements
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
import sys
import os
 
rootdir = os.path.dirname(os.path.abspath(os.path.basename(__file__)))
print(rootdir)
sys.path.append(rootdir)

from src.utils import change_wd_to_current_file

change_wd_to_current_file()

# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = pd.read_csv('../27_Regularization/data.csv', header=None)
X = train_data.iloc[:,:-1]
y = train_data.iloc[:,-1]

# TODO: Create the standardization scaling object.
scaler = StandardScaler()

# TODO: Fit the standardization parameters and scale the data.
X_scaled = scaler.fit_transform(X)

# TODO: Create the linear regression model with lasso regularization.
lasso_reg = Lasso()

# TODO: Fit the model.
lasso_reg.fit(X_scaled, y)


# TODO: Retrieve and print out the coefficients from the regression model.
reg_coef = lasso_reg.coef_
print(reg_coef)