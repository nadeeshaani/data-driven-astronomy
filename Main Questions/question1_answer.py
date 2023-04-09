import numpy as np

def list_stats(values):
# defines a function called `list_stats` that takes a 
# single arument `values`
    
    N = len(values)
    if N == 0:
       return
'''These two lines calculate the length of the values list 
using the len function
 and store the result in N. 
If N is equal to 0, 
then the function immediately returns without performing any further calculations.'''

    # Mean
    mean = sum(values)/N
'''This line calculates the mean of the values list by
 summing all the elements in the list using the sum function 
and dividing the result by the length of the list, 
which is stored in N. The result is stored in the mean variable.'''


    # Median
    values.sort()
    mid = int(N/2)
    if N%2 == 0:
        median = (values[mid] + values[mid - 1])/2
    else:
        median = values[mid]

    return median, mean
'''These lines calculate the median of the values list. 
First, the list is sorted using the sort method of lists in Python. 
Then, the middle index of the list is calculated as mid. 
If the length of the list is even, 
then the median is the average of the values at indices mid and mid-1.
 If the length of the list is odd, 
then the median is the value at index mid.'''

#and finally the function returns a tuple of two values



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)
