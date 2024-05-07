import pandas as pd

# DataFrame helps to arrange data in table format
d = {'col': [1,2,3,4,7], 'col2': [4, 5, 6, 9, 5], 'col3':[7, 8, 12, 1, 11]}

df = pd.DataFrame(data = d)

# We can count the number of columns and rows using shape[]
# columns are identified by 1 while
# rows are identified by 0


count_row = df.shape[0]
count_column = df.shape[1]


print(df)
print("Number of columns: ", count_column)
print("Number of rows: ", count_row)



