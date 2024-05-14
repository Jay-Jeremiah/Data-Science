import pandas as pd
import numpy as np


full_health_data = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\DataScience\\Data-Science\\CSV_files\\data15.csv')

Calories = full_health_data["Calorie_Burnage"]

percent25 = np.percentile(Calories, 25)

print("The 25th percentile is ", percent25)