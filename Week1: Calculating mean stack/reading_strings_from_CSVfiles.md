
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
