from typing import List


class Solution:
    def removeElementWell(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
    
    def removeElementTP(self, nums: List[int], val: int) -> int:
        i = 0
        l,r = 0, len(nums)-1
        while len(nums) > 0 and l <= r:
            if l < len(nums) and nums[l] == val:
                nums.pop(l)
            else:
                l+=1
            if r < len(nums) and nums[r] == val:
                nums.pop(r)
            else:
                r-=1
        return len(nums)
    
    def removeElementBad(self, nums: List[int], val: int) -> int:
        a = []
        for i,v in enumerate(nums):
            if v != val:
                a.append(v)
        al = len(a) -1
        for i,v in enumerate(nums):
            if i <= al:
                nums[i] = a[i]
            else:
                nums[i] = None
        return len(a)
