import pandas as pd 
import numpy as np 

full_health_data = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\DataScience\\Data-Science\\CSV_files\\data15.csv')

Max_Pulse = full_health_data["Max_Pulse"]


percentile10 = np.percentile(Max_Pulse, 10)

print(percentile10)