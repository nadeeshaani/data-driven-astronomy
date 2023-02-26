'''Write a `calc_stats` function that reads data from a CSV file and calculates its mean and the median. Your function should take the name of the file as an argument and return the mean and median in a tuple, rounded to one decimal place.

The function should work like this,

>>> calc_stats(’data.csv’)

(11.1, 11.4)

1st value → mean

2nd value → median

Your solution cannot use the builtin `statistics` module.'''


# Write your calc_stats function here.
import numpy as np

def calc_stats(filename):
  data = np.loadtxt(filename, delimiter=",")
  
  mean = np.mean(data)
  median = np.median(data)
  
  return np.round(mean, 1), np.round(median, 1)
  
  

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean_n_median = calc_stats('data.csv')
  print(mean_n_median)
  
  mean_n_median = calc_stats('data2.csv')
  print(mean_n_median)
  
  mean_n_median = calc_stats('data3.csv')
  print(mean_n_median)
