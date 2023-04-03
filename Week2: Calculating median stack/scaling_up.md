### Scaling up to large arrays

- We can easily calculate the size of NumPy arrays in memory.
- In a previous activity, we used FITS images with 200 x 200 pixels stored in (200, 200) arrays.
- Each element in the array is a NumPy float32, which requires 4 bytes of memory.
- The size of the entire array is calculated by multiplying the number of pixels by the number of bytes per pixel (4).
- The size of the array in this example is 156.25 kB (divided by 1024).
- If we have tens or thousands of arrays, the memory usage can quickly become significant.
- We can calculate the memory usage for 1000 and 10,000 arrays by multiplying the size of a single array by the number of arrays.
- Typical astronomy images are often larger than 200 x 200 pixels, which means that the memory usage can be even greater than in this example.
