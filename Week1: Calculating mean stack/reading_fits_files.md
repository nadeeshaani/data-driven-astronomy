- Opening a FITS file in Astropy returns,
    - a HDU list → Header/data unit list.

- Each HDU stores,
    - headers
    - image data (optional)

- Accessing individual HDUs
    
    ```python
    from astropy.io import fits
    
    hdulist = fits.open('image0.fits')
    data = hdulist[0].data
    
    print(data.shape)
    ```
