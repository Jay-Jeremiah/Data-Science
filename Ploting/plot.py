# ploting graphs, we use the plot() function
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


# import the data set
health_data = pd.read_csv('dt.csv')
print(health_data)


# identify the x and y values from the data set
health_data.plot(x = 'Average_Pulse',y = 'Calorie_Burnage', kind='line')

# indicate the starting points of the axes using plt.ylim and plt.xlim
plt.ylim(ymin=0)
plt.xlim(xmin=0)

# plt.show() function shows the output of the graph
plt.show()



