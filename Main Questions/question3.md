### Question 3

Implement the binapprox algorithm to calculate the median of a list of numbers.

Do the wholen implementation by writing these two functions:

1. `median_bins` → to calculate mean, standard deviation and the bins
    
    ```python
    median_bins(values, B)
    ```
    
    - This function takes following as input,
        - a list of values
        - the number of bins, `B`
    - Returns,
        - the mean $\mu$
        - standard deviation $\sigma$
        - the number of values smaller than $\mu - \sigma$
        - A NumPy array with B elements containing the bin counts
    - e.g.,
        
        ```python
        >>> median_bins([1, 1, 3, 2, 2, 6], 3)
        (2.5, 1.707825127659933, 0, array([ 2.,  3.,  0.]))
        ```
        
    
2. `median_approx` → calls the `median_bins` and then calculates the approximated median 
    - The function takes following as input,
        - A list of values
        - The number of bins, `B`
    
    - The function returns following as output,
        - It should return the approximate median using `median_bins`to calculate the bins
    
    - e.g.,
        
        ```python
        >>> median_approx([1,1,3,2,2,6], 3)
        2.5
        ```
        

To make sure your functions work for the general case, here's another example which uses four bins:

```python
>>> median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4)
(3.875, 2.521780125229002, 3, array([ 0.,  1.,  1.,  1.]))
>>> median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4)
4.50544503130725
```

Here's an example in which binapprox is a bad approximation:

```python
>>> median_bins([0, 1], 5)
(0.5, 0.5, 0, array([ 1.,  0.,  0.,  0., 0.]))
>>> median_approx([0, 1], 5)
0.90000000000000002
```
