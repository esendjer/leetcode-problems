# 153. Find Minimum in Rotated Sorted Array

[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

Here are a couple of ways to solve the problem:
* Binary search - function `findMin`
* Python `min` - function `findMinPyNative`

Rhe first way with the Binary search implies O(log n) complexity,
but the thing is that the embedded `min` function is realized on a lowest C level and works faster regardless of its O(n) complexity.

Time Complexity of some operations in current CPython - https://wiki.python.org/moin/TimeComplexity

A bit more information about the Binary search:
* https://www.geeksforgeeks.org/python-program-for-binary-search/
* https://www.programiz.com/dsa/binary-search
* https://realpython.com/binary-search-python/
  * https://realpython.com/binary-search-python/#binary-search

# Hints/tips
* Array was originally in ascending order. Now that the array is rotated, there would be a point in the array where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].
* You can divide the search space into two and see which direction to go. Can you think of an algorithm which has O(logN) search complexity?
* All the elements to the left of inflection point > first element of the array. All the elements to the right of inflection point < first element of the array.
