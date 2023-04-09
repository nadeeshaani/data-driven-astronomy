### Question 1

Write a function called `list_stats` that takes a list of numbers and returns a tuple of the median and mean of the list (in this order).

The function should work on lists with even or odd numbers of elements and handle the case of a one-element list.

**Your solution cannot use the builtin `statistics` module.**

Here's an example of how your function should work:

`>>> list_stats([1.3, 2.4, 20.6, 0.95, 3.1])`

`(2.4, 5.67)`

Where `2.4` is the median and `5.67` is the mean.

Your function should work on lists with even and odd numbers of elements. Here's an example using an even-length list:

`>>> list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])`

`(2.55, 5.175)`

For a one element list, the median and mean should be the same:

`>>> list_stats([1.5])`

`(1.5, 1.5)`

