import sys
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def __init__(self):
        self.ans = sys.maxsize
        self.prev = self.ans
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return self.ans
        self.getMinimumDifference(root.left)
        if self.prev != sys.maxsize:
            self.ans = min(self.ans, root.val - self.prev)
        self.prev = root.val
        self.getMinimumDifference(root.right)
        return self.ans

class Solution2:
    def bst_to_sorted_list(self, root, l):
        if not root:
            return
        self.bst_to_sorted_list(root.left, l)
        l.append(root.val)
        self.bst_to_sorted_list(root.right, l)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sort_list = []
        self.bst_to_sorted_list(root, sort_list)
        ans = sys.maxsize
        for i in range(1, len(sort_list)):
            ans = min(ans, sort_list[i] - sort_list[i-1])
        return ans