

- When comparing algorithms, it's important to consider their memory usage as well as their speed.
- To create memory-efficient algorithms, it's necessary to understand how Python uses memory.
- Which module in python allows to check memory usage?
    - `sys` module

- e.g., code to understand Python’s memory usage
    
    ```python
    import sys
    
    a = 3
    b = 3.123
    c = [a, b]
    d = []
    for obj in [a, b, c, d]:
      print(obj, sys.getsizeof(obj))
    ```
    
    output:
    
    When the code is run, it shows that 
    
    - an integer uses 14 bytes,
    - a float uses 16 bytes,
    - and a list containing the two uses 40 bytes.
    
    Explanation:
    
    - The memory used by the list **`c`**is not the sum of the sizes of **`a`**and **`b`**
    - Firstly, there is overhead for the list itself (the empty list **`d`**is 32 bytes).
    - Secondly, the list does not contain the objects themselves, but instead holds references to the other objects in memory.
