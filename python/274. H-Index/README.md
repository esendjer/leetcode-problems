# 274. H-Index

[274. H-Index](https://leetcode.com/problems/h-index/description/)

The problem was solved in a few ways:
* `hIndex` - usage of Python's _heap_ 
* `hIndexW` - similar to _heap_ using approach, but with a list sorting

_heappop_ has O(log n) but happens at each iteration of the while loop, and _sort_ has O(n log n) time complexity. So that, both of the solutions here have (at least it looks so) similar time O(n log n) and O(1) extra space complexity,