# we use the describe() attribute to summarise data in the data set

import pandas as pd


critical = pd.read_csv('C:\\Users\\Jeremiah\Documents\\DataScience\\Data-Science\\Statsistics\\data14.csv')

pd.set_option('display.max_columns', None)

pd.set_option('display.max_rows', None)

print(critical.describe())