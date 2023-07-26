from typing import List


class Solution:
    def twoSumS(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(nums):
            l = target - v
            if l in d:
                return d[l], i
            else:
                d[v] = i
        return 0,0
    
    def twoSumF(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            pas = prev.get(target - nums[i])
            if not pas is None:
                return [pas, i]
            prev[nums[i]] = i
        