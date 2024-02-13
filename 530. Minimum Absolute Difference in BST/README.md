# 530. Minimum Absolute Difference in BST

https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

## Solution1

* Time complexity: ${O(n)}$, it touche each node just once
* Space complexity: ${O(h)}$, if consider the stack of recursive calls the function (in-order traversal through the BST), where `h` - is a hight of the BST, for the average scenario. Meanwhile, the worse case is ${O(n)}$.

## Solution2

* Time complexity: ${O(n)}$ for in-order traversal through the BST (`bst_to_sorted_list`) + `for` loop to find out the minimum absolute difference => ${O(n) + O(n) => O(n)}$
* Space complexity: ${O(h)}$ for the stack of recursive calls the function (in-order traversal through the BST) + ${O(n)}$ for the extra array (list) of in-order storage of all the values => ${O(h) + O(n) => O(n)}$