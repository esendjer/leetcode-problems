# 100. Same Tree

[100. Same Tree](https://leetcode.com/problems/same-tree/description/)

- **Space complexity**: due to recursion applied here (the entire stack of calls) will have ${ O(log n) + O(log m) => O(log n) }$ on the average and ${ O(log n) + O (log m) => O(n) }$ on the worst cases; where `n` & `m` are nodes of the `q` and `p` trees.
- **Time complexity**: there is no repeated touches of nodes, so that it's ${ O(log n) + O (log m) => O(n) }$