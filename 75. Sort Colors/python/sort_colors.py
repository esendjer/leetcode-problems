from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        o = 0
        t = 0
        for i in nums:
            if i == 0:
                z += 1
            elif i == 1:
                o += 1
            else:
                t += 1
        for i in range(z):
            nums[i] = 0
        for i in range(z,z+o):
            nums[i] = 1
        for i in range(z+o,z+o+t):
            nums[i] = 2
    