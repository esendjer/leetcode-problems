# 637. Average of Levels in Binary Tree

[637. Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150)

- **Space**: ${O(n)}$ extra storage for nodes' values on each level + stack of calls ${ O(log n) }$, so that ${ O(n) + O(log n) => O(n)}$ or on the worst case ${O(n) + O(n) => O(n)}$
- **Time**: ${O(n) + O(l+m) => O(n)}$; where `n` - tree's nodes, `l` tree's levels, `m` tree's nodes on the level

