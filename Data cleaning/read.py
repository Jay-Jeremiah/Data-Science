# Data Cleaning is rmoving the blank cells from the data set

import pandas as pd

health_data = pd.read_csv('data.csv')

print(health_data)

# all blank cells are automically converted into NaN values 
# To remove NaN values, we use dropna() function with axis=0 which removes all NaN values at once

a = health_data.dropna(axis=0)

print(a)


