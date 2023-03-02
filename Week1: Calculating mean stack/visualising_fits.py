from astropy.io import fits
"""The astropy.io.fits library provides functions for 
reading and writing FITS files, which are a standard file format for storing astronomical data."""

import matplotlib.pyplot as plt
# matplotlib.pyplot library provides functions for creating data visualizations

hdulist = fits.open('image0.fits')
"""reads in a FITS file called 'image0.fits' 
using the fits.open function from the astropy.io.fits library."""

data = hdulist[0].data
'''The data from the FITS file is stored in a 2D array,
which is accessed using the hdulist[0].data statement. 
The hdulist variable is a HDUList object, 
which contains all the headers and data in the FITS file'''

# Plot the 2D array

plt.imshow(data, cmap=plt.cm.viridis)
'''Then, the code creates a visualization of the data using the plt.imshow function
from the matplotlib.pyplot library. 
This function displays a 2D array as an image, 
with each pixel in the array corresponding to a pixel in the image.'''

'''The cmap argument specifies the color map to use for the image, 
in this case the viridis color map.'''

plt.xlabel('x-pixels (RA)')
plt.ylabel('y-pixels (Dec)')
'''The plt.xlabel and plt.ylabel functions set the labels for 
the x and y axes of the plot, respectively.'''

plt.colorbar()
'''The plt.colorbar function adds a color bar to the plot 
to indicate the color mapping.

plt.show()
''' Finally, the plt.show function displays the plot on the screen.'''
