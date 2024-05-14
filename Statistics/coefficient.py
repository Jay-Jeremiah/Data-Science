# coefficient of variable is used to get the idea of how large the standard deviation is
# It is calculated by dividing the standard deviation with the mean

import pandas as pd 
import numpy as np

details = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\DataScience\\Data-Science\\CSV_files\\data16.csv')

Salaries = details["Salary"]

std = np.std(Salaries)

mean = np.mean(Salaries)

coeff = std/mean

print(coeff)
