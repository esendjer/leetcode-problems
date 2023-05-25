# 33. Search in Rotated Sorted Array

[33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

Here are three solutions:
* `search` - dumb, but very simple, has O(n) complexity due to it's how _index_ and _in_ work in Python - 57 ms
* `searchCouplesFor` - searches through couples of indexes in _for_ loop - 63 ms
* `searchCouplesWhile` - searches through couples of indexes in _while_ loop (looks faster then _for_ loop) - 48 ms
* `searchBSClean` - a Binary Search - 60 ms
* `searchBSCouples` - a Binary Search with searching through 3 indexes (left, middle, right) within one iteration - 50 ms
