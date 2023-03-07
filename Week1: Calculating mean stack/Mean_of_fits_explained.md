Explanation bit by bit,

- These lines import the required libraries **`astropy.io`**and **`numpy`**
.
    
    ```python
    from astropy.io import fits
    import numpy as np
    ```
    
- Creating the function `mean_fits` that takes a list of FITS file names as an input (`files`)
    - Calculating the number of files in the list,
        
        `n = len(files)`
        
    - checks if the list is not empty,
        
        **`if n > 0:`**
        
    
    - Opening the first file in the list
        
        **`hdulist = fits.open(files[0])`**
        
        —> using the `[fits.open](http://fits.open)` function provided by `astropy.io`
        
    - Reading the data from the first file using the `data` attribute of the `HDUList` object,
        
        `data = hdulist[0].data`
        
    
    - closing the file,
        
        `hdulist.close()`
        
    - Reading data from each file (second to last file) and adding it to the data variable
        
        `for` loop does this
        
        ```python
        for i in range(1, n):
              hdulist = fits.open(files[i])
              data += hdulist[0].data
              hdulist.close()
        ```
        
    - calculating the mean variable
        
        ```python
        mean = data / n
            return mean
        ```
        
    - Running the `mean_fits` function on a list of FITS file names
        
        ```python
        data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
        ```
        
    - Printing the value of the pixel at position (100, 100) of the resulting data
        
        ```python
        print(data[100, 100])
        ```
        
    - Importing matplotlib.pyplot library as plt, and then using it to display the mean data as an image using `imshow` function
        
        ```python
        import matplotlib.pyplot as plt
          plt.imshow(data.T, cmap=plt.cm.viridis)
        ```
        
        - The **`cmap`**argument specifies the color map to use.
        - **`plt.cm.viridis`** specifies the **`viridis`**color map.
    
    - Adding a color bar to the plot
        
        ```python
        plt.colorbar()
        ```
        
    
    - Displaying the plot,
        
        ```python
        plt.show()
        ```
