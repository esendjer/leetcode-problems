# 162. Find Peak Element

The solutions:
* `findPeakElementBS` - uses Binary Search
* `findPeakElement` - does search in 2 directions _0 -> Middle <- -1_, and checks both _i_ and _-1-i_ on each iteration
* `findPeakElementSecondWay` - does search in one direction _0 -> End_, and checks _i_ and _i+1_ on each iteration

There is the possibility to solve the problem with usage of Python's `max` embedded function.