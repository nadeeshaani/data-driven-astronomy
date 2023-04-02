### memory footprint of NumPy arrays

- NumPy arrays are more compact than regular Python data structures, and thus, their memory usage is worth exploring.

- *To get the total size of a NumPy array we can use following ways,*
    - `getsizeof` function of `sys` module
        - but this value will always be larger than the actual data size because NumPy arrays contain metadata about the data type, shape, and other properties.
    - using `nbytes` attribute
        - To get the memory usage of the data itself, we can use the nbytes attribute, which gives the number of bytes used by the array data.

- *Let’s compare their performance and results with following code,*
    
    ```python
    import sys
    import numpy as np
    
    a = np.array([])
    b = np.array([1, 2, 3])
    c = np.zeros(10**6)
    
    for obj in [a, b, c]:
      print('sys:', sys.getsizeof(obj), 'np:', obj.nbytes)
    ```
    
    output :
    
    getsizeof returns a larger value than nbytes attribute
    

- *We can calculate the `nbytes` as follows,*
    - value by multiplying the number of elements with the size in bytes of each element.
        
        $nbytes = number \space of \space elements \times each \space element \space size  \space in \space bytes$
        
- 
    
    ```python
    	import numpy as np
    
    a = np.zeros(5, dtype=np.int32)
    b = np.zeros(5, dtype=np.float64)
    
    for obj in [a, b]:
      print('nbytes         :', obj.nbytes)
      print('size x itemsize:', obj.size*obj.itemsize)
    ```
    
    explanation of the code:
    
    - In the provided code, two NumPy arrays of the same shape but with different data types are created.
    - The first array is of integer type (int32), and the second array is of floating-point type (float64).
    - The code then iterates over the two arrays and prints out the nbytes and size x itemsize values for each array.
    - The size x itemsize value is the product of the array's size and itemsize attributes, which should be equal to the nbytes value.
    - This demonstrates the relationship between the number of elements in the array, the size of each element, and the total memory used by the array's data.
