## Calculating median without using statistics module

- First step will always be sorting the data.
#### When the number of values are odd

  ```python
  fluxes = [17.3, 70.1, 22.3, 16.2, 20.7]
  fluxes.sort()
  mid = len(fluxes)//2
  median = fluxes[mid]
  print(median)
  ```

#### When number of values are even
  - Then there will be two middle values.
  - So we take the both middle values and take the average → that is median

  ```python
  fluxes = [17.3, 70.1, 22.3, 16.2, 20.7, 19.3]
  fluxes.sort()
  mid = len(fluxes)//2
  median = (fluxes[mid - 1] + fluxes[mid])/2
  print(median)
    ```
