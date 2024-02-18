# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.levels = {}  # dict
    
    def levels_avg(self, node, level=0):
        if node is None:
            return
        self.levels_avg(node.left, level+1)
        self.levels_avg(node.right, level+1)

        if level not in self.levels:
            self.levels[level] = [node.val]
        else:
            self.levels[level].append(node.val)

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return
        self.levels_avg(root)
        ans = []
        for i in range(len(self.levels)):
            ans.append(sum(self.levels[i]) / len(self.levels[i]))
        return ans
        