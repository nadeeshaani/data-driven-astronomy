- One problem can have many implementations.
- To check which implementation is better, we can time our programs
- One way to do this is Python’s time module.
    
    
    ```python
    import time
    start = time.perf_counter()
    # potentially slow computation
    end = time.perf_counter() - start
    ```
    
### Timing our code

let’s compare the timing of two functions.

- Let’s compare the time it takes to do the following calculation when done using handwritten code vs NumPy’s mean function

Handwritten code:

```python
import time, numpy as np
n = 10**7
data = np.random.randn(n)

start = time.perf_counter()
mean = sum(data)/len(data)
seconds = time.perf_counter() - start

print('That took {:.2f} seconds.'.format(seconds))
```

using Numpy mean function

```python
import time, numpy as np
n = 10**7
data = np.random.randn(n)

start = time.perf_counter()
mean = np.mean(data)
seconds = time.perf_counter() - start

print('That took {:.2f} seconds.'.format(seconds))
```

The second code outperforms first one.
