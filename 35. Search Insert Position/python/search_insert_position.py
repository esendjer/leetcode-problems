from typing import List

class Solution:
    def searchInsertTP(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        while l<=r:
            if nums[l] >= target:
                return l
            else:
                l +=1
            if nums[r] == target:
                return r
            elif nums[r] < target:
                return r+1
            else:
                if l<=r-1:
                    r -=1
    
    def searchInsertN(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i,v in enumerate(nums):
            if v == target or v > target:
                return i