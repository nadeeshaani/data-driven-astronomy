# Explanation of each code line in brigtest_pixel.py

```python
from astropy.io import fits
import numpy as np
```

- Here, we are importing two modules - **`fits`**
 from **`astropy.io`** and **`numpy`**as **`np`**
- . **`fits`**is a module that allows us to read data from FITS files
- **`numpy`** is a module that provides numerical operations on arrays and matrices.
- This allows us to visually confirm the location of the brightest pixel in the image.

```python
def load_fits(filename):
    hdulist = fits.open(filename)
    data = hdulist[0].data
```

- load_fits function takes `filename` argument.
- First opens the FITS file using `[fits.open](http://fits.open)` → it returns a `hdulist` object
- The `hdulist` object contains Header Data Units. (one or more)
- Then we are taking the first HDU → hence, `hdulist[0]`
- Then we use `data` attribute to extract the data from the HDU


```python
arg_max = np.argmax(data)
max_pos = np.unravel_index(arg_max, data.shape)
```

- Here we are finding the position of the brightest pixel in the imagae
- **`arg_max`**is the index of the maximum value in the flattened **`data`** array.
- We then use **`np.unravel_index`** to convert this flat index back into the 2D index of the maximum value in the **`data`**array.

```python
return max_pos
```

Finally, the function returns the position of the brightest pixel in the image.

```python
if __name__ == '__main__':
    bright = load_fits('image1.fits')
    print(bright)
```

- This is the main part of the code that runs when the script is executed.
- Here, we call the **`load_fits`** function with the filename **`'image1.fits'` then,** store the result in the variable **`bright`**
- We then print the position of the brightest pixel in the image.


```python
hdulist = fits.open('image1.fits')
    data = hdulist[0].data

    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()
```

- Finally, we open the FITS file again
- extract the data, and use **`plt.imshow`**
 to display the image.
- We use **`data.T`** to transpose the data array so that the x and y axes are displayed correctly
- and **`cmap=plt.cm.viridis`t**o set the colormap to 'viridis'.
- We also add a colorbar using **`plt.colorbar()`**
- and display the plot using **`plt.show()`**
This allows us to visually confirm the location of the brightest pixel in the image.

