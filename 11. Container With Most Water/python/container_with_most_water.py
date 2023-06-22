from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        fp = 0
        lp = len(height) - 1
        while lp > fp:
            v = min(height[fp], height[lp]) * (lp - fp)
            if m < v:
                m = v
            if height[fp] < height[lp]:
                fp += 1
            else:
                lp -= 1
        return m