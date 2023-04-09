# Write your median_bins and median_approx functions here.

'''This code contains two functions, median_bins and median_approx, 
which are used to calculate the median of a given set of values.'''

import numpy as np

'''The function below takes two arguments, 
values and B, 
where values is a list of numbers and 
B is the number of bins we want to use to calculate the median.'''
def median_bins(values, B):
	''' calculating the mean using NumPy library'''
  mean = np.mean(values)

	''' calculating the standard deviation using NumPy'''
  std = np.std(values)
    
  # Initialise bins
  left_bin = 0 
	'''this keeps the track of the number of values 
		that fall below the range of bins'''

  bins = np.zeros(B)
	'''NumPy array that will store the number of values 
that fall within each bin'''

  bin_width = 2*std/B
	'''the width of each bin'''
    
  # Bin values

  for value in values:
    if value < mean - std:
      left_bin += 1
    elif value < mean + std:
      bin = int((value - (mean - std))/bin_width)
      bins[bin] += 1
    # Ignore values above mean + std

''' the above secion -->
iterates through each value in the input list 
and assigns it to an appropriate bin based on its value. 
If a value falls below the range of bins, it increments the left_bin variable. 
If a value falls within the range of bins, 
it calculates which bin it should belong to 
and increments the count of that bin in the bins array. 
If a value falls above the range of bins, it is ignored.'''

  return mean, std, left_bin, bins
'''Finally, this function returns the mean, standard deviation, left_bin, and bins 
so that they can be used to calculate the median using the median_approx function.'''


'''The function below also takes two arguments, values and B, 
where values is a list of numbers and B is the number of bins used in the median_bins function.'''
def median_approx(values, B):
  # Call median_bins to calculate the mean, std,
  # and bins for the input values
  mean, std, left_bin, bins = median_bins(values, B)
    	
  # Position of the middle element
  N = len(values)
  mid = (N + 1)/2


'''this section below--> iterates through the bins array 
and keeps track of the cumulative count of values as it goes. 
When the cumulative count exceeds the midpoint, 
it breaks out of the loop and calculates the median using the bin index (b) and bin width.'''

  count = left_bin
  for b, bincount in enumerate(bins):
    count += bincount
    if count >= mid:
      # Stop when the cumulative count exceeds the midpoint
      break

  width = 2*std/B
  median = mean - std + width*(b + 0.5)
  return median



# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
