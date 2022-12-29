# TODO: Add import statements
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import os, sys

rootdir = os.path.dirname(os.path.abspath(os.path.basename(__file__)))
print(rootdir)
sys.path.append(rootdir)

from src.utils import change_wd_to_current_file

change_wd_to_current_file()

# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = pd.read_csv('bmi.csv')

# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()
reg = bmi_life_model.fit(bmi_life_data[['BMI']], bmi_life_data[['Life expectancy']])

# Make a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
laos_life_exp = reg.predict([[21.07931]])
print(f'laos_life_exp is {laos_life_exp}')