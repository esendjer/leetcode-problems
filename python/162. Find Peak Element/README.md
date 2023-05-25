# 162. Find Peak Element

Both ways that this problem is solved here use Binary search:
* `findPeakElement` - does search in 2 directions _0 -> Middle <- -1_, and checks both _i_ and _-1-i_ on each iteration
* `findPeakElementSecondWay` - does search in one direction _0 -> End_, and checks _i_ and _i+1_ on each iteration