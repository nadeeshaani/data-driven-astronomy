- We can construct a multi-dimensional array from a nested list.  (a list within a list)
- To access columns or rows of a multi-dimensional array, we use,
    - a method calls → slicing

- e. g.,
    
    ```python
    import numpy as np
    
    a = np.array([[1,2,3], [4,5,6]])  # 2x3 array
    
    # Print first row of a:
    print(a[0,:])
    
    # Print second column of a:
    print(a[:,1])
    ```
