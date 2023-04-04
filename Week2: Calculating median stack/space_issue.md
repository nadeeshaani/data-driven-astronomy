### Saving space issue

- Calculating the median requires all the data to be in memory at once.
- This is a problem in astrophysics calculations, which may involve hundreds of thousands of FITS files.
- Even with a machine with lots of RAM, it's not possible to find the median of more than a few tens of thousands of images.
- This is not an issue for calculating the mean, since the sum only requires one image to be added at a time.
- You can load an image, add it to the sum, and then reuse the memory.
- Since the sum is only ever the size of a single image, you'll never run out of memory.
