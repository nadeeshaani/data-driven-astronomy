
- *What are CSV files?*
    - Comma-separated values.
    - Tables are often stores in CSV format
    
- We have the following CSV file called `data.csv`
  
  
  ![image](https://user-images.githubusercontent.com/90096354/221406084-c7623df9-8c66-4514-91c3-4a3632583895.png)

    
- Now we want to store,
    - each row in a list
    - whole data.csv file as a list of these rows.

- This is how it’s done,
    
    ```python
    data = []
    for line in open('data.csv'):
      data.append(line.strip().split(','))
    
    print(data)
    ```
    
    Explanation of the above program,
    
    - The program loops over each line in the file, splitting the row into a list of values, and appending each row to `data`
    - strip method → it removes whitespaces (+new lines) from the end of line
    - split method → it creates a list of strings using ‘,’ character as the separator between them.
    - Now we should remember that the above Python program returns a list of strings.


- Since the `split`method returns a list of strings, so each value in each row is a string. We have to convert the values to floats before we can do any calculations with them.
- To convert each item from a string to a float, we can use one of following ways,
    - Using nested for loops,
        
        ```python
        data = []
        for line in open('data.csv'):
          row = []
          for col in line.strip().split(','):
            row.append(float(col))
          data.append(row)
        
        print(data)
        ```
        

- Using `asarray` function in NumPy
    
    ```python
    import numpy as np
    
    data = []
    for line in open('data.csv'):
      data.append(line.strip().split(','))
    
    data = np.asarray(data, float)
    print(data)
    ```
    
    * Most NumPy functions operate on the whole array at once (rather than individual items)
