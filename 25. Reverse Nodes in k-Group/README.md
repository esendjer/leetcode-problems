# 25. Reverse Nodes in k-Group

[25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)

It's needed there to reverse a sub-list of `k` elements at time through entire list, if the number of items is not a multiple of `k` they have to remain untouched, as it is.

This solution has the complexities as follows:
* Time: $O(2n)$ (explained below) -> $O(n)$
* Space: $O(1)$

## Explanation

There are some additional variables to store temporary data (`dummy` node and links), but the amount of them is constant, so that solution's Space complexity is $O(1)$, as required there.

The total Time complexity is $O(2n)$, because if two `for` loops.

* The first `for` loop makes reversing of `k` elements, and there is `range` of `k-1` since to reverse array of `k` items the number of iteration has to be `k-1`.

* The second loop just checks how many elements remain in the list, since that it has `range` of `k`.

Overall, it iterates through a list twice - $O(2n)$, we can drop constant and get $O(n)$.
