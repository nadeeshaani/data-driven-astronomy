import time, numpy as np
from astropy.io import fits
# This line imports the required modules for the script: time, numpy, and astropy.io.fits


def median_fits(filenames):
# defines a function median_fits that takes a list of filenames as an input.

  start = time.time()   
	# Start timer
	'''This line gets the current time and assigns it to the variable start, 
		which will be used to calculate the elapsed time.'''




  # Read in all the FITS files and store in list
  FITS_list = []
  for filename in filenames: 
    hdulist = fits.open(filename)
    FITS_list.append(hdulist[0].data)
    hdulist.close()
'''These lines open each file in the filenames list 
using the fits.open() method from the astropy.io.fits module. 
It then extracts the data from the first extension (hdulist[0].data) 
and appends it to a list called FITS_list. 
Finally, the file is closed using the hdulist.close() method'''


  # Stack image arrays in 3D array for median calculation
  FITS_stack = np.dstack(FITS_list)
'''This line stacks the 2D image arrays in the FITS_list into a 
3D array called FITS_stack using the np.dstack() function from the numpy module. 
The resulting array has dimensions (N, M, P) where N and M are the dimensions of the image 
and P is the number of input files.'''


  median = np.median(FITS_stack, axis=2)
'''This line calculates the median along the third axis of the FITS_stack array 
using the np.median() function from the numpy module. 
This calculates the median for each pixel across all input files.'''


  # Calculate the memory consumed by the data
  memory = FITS_stack.nbytes
  # or, equivalently:
  #memory = 200 * 200 * len(filenames) * FITS_stack.itemsize

  # convert to kB:
  memory /= 1024

'''These lines calculate the amount of memory consumed by the data. 
The nbytes attribute of the FITS_stack array gives the total number of bytes used by the array, 
and dividing this by 1024 converts it to kilobytes. 
Alternatively, the amount of memory can be calculated by multiplying the number of pixels 
(which is 200 x 200 in this case) by the number of files and the size of each pixel (given by FITS_stack.itemsize). 
The result is also divided by 1024 to give the memory usage in kilobytes.'''

  
  stop = time.time() - start   # stop timer
  return median, stop, memory
'''These lines calculate the elapsed time by subtracting the start time from 
the current time (time.time()) 
and assigning the result to the variable stop. 
The function then returns 
the median array, the elapsed time, and the memory usage in kilobytes as a tuple.'''

if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])
