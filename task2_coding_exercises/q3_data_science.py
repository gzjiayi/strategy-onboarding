"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

# Your code here
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/grace/Midnight Sun/strategy-onboarding/task2_coding_exercises/q3_test_data.csv', header = None)

print(data)

#check for missing data points
print(data.isnull().sum())

#drop rows with missing values
data = data.dropna()

data.plot()
plt.show()

plt.savefig('\q3_plots')

