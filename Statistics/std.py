# standard deviation is a number that describes how observations are spread out.
# we use the std() attribute to calculate it

import pandas as pd

# std() attribute is got from numpy

import numpy as np

details = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\DataScience\\Data-Science\\CSV_files\\data16.csv')

Salary = details["Salary"]

std = np.std(Salary)

print(std)