### Why use median?

#### Why mean fails sometimes…
- When there are outliers in the data set, mean can not be a good representation
        
```python
from statistics import mean
fluxes = [17.3, 70.1, 22.3, 16.2, 20.7]
m = mean(fluxes)
print(m)
```

Mean → with outlier (70.1) = 29.34

Mean → without outlier = 19.125

#### But median works just fine even in those times..
- The median is defined simply as the middle of the sorted data set.
- Since only the order of the data points matters, not their value, outliers have much less of an effect on median.
- Thus, median is a good representation

```python
from statistics import median
fluxes = [17.3, 70.1, 22.3, 16.2, 20.7]
m = median(fluxes)
print(m)
```
