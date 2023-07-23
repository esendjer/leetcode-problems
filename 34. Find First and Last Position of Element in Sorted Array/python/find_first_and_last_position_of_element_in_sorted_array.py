from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = [-1,-1]
        if not len(nums):
            return a
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == target:
                if a[0] == -1 or a[0] > l:
                    a[0] = l
                if l > a[1]:
                    a[1] = l
            if nums[r] == target:
                if a[1] < r:
                    a[1] = r
                if a[0] == -1 or r < a[0]:
                    a[0] = r
            l += 1
            if r - 1 > l:
                r-=1
        return a
