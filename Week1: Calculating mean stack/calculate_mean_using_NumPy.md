### In this, we are going to calculate the mean with a NumPy array

- [NumPy](http://www.numpy.org/) arrays can store purely numerical data
    - in much less space,
    - much simpler for calculations
    - faster for calculations.

- Calculating the mean with a NumPy array instead of a list,
    
    ```python
    import numpy as np
    
    fluxes = np.array([23.3, 42.1, 2.0, -3.2, 55.6])
    
    m = np.mean(fluxes)
    
    print(m)
    ```
    
#### NumPy has a great range of numerical functions.

1. calculating the size of an array → using NumPy `size` function
    
    ```python
    import numpy as np
    fluxes = np.array([23.3, 42.1, 2.0, -3.2, 55.6])
    print(np.size(fluxes)) # length of array
    ```
    
2. Calculating the standard deviation of an array,

    ```python
    import numpy as np
    fluxes = np.array([23.3, 42.1, 2.0, -3.2, 55.6])

    print(np.std(fluxes))  # standard deviation
    ```
