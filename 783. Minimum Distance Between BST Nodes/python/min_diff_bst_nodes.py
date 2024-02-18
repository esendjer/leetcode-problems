import sys
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None
        self.ans = sys.maxsize
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        _ = self.minDiffInBST(root.left)
        if self.prev is None:
            self.prev = root.val
        else:
            self.ans = min(self.ans, root.val - self.prev)
            self.prev = root.val
        _ = self.minDiffInBST(root.right)
        return self.ans
        