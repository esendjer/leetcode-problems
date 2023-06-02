# 136. Single Number

[136. Single Number](https://leetcode.com/problems/single-number/)

Solved with sorted arr and heap, but there is a way with sort + binary search:

```
[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,10,10,11,12,12,13,13,14,14]
                         ^m
len = 25
25 // 2 = 12
12 - we expect that each even number is the first from repeated pair
13 - and each odd number is the second

if i[12] == i[13] means that the single is on the right side
if i[12] != i[13] means that the single is on the left side
...
```
