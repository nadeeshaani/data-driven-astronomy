- *What are FITS files?*
    - Flexible Image Transport System files.
    - In a FITS file, the image is stored in a numerical array.
    - We can load that numerical array into a NumPy array.



- *Here are some other characteristics of FITS files,*
    - FITS files have headers → inside these headers they store metadata about the image
    - FITS files are a standard format and astronomers have developed many libraries  that can read and write FITS files.



- *Here in this course, to read and write FITS files we are using the module,*
    - Astropy



- *How to open a FITS file?*
    
    ```python
    from astropy.io import fits
    hdulist = fits.open('image0.fits')
    ```
    
    
- *How to print out the header information included in a FITS file?*
    
    ```python
    from astropy.io import fits
    hdulist = fits.open('image0.fits')
    hdulist.info()
    ```
    
    
    output →
    
    ```
    Filename: test0.fits
    No.    Name         Type      Cards   Dimensions   Format
    0    PRIMARY     PrimaryHDU       7   (200, 200)   float64
    ```
