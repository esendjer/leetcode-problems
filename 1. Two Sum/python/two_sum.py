from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            pas = prev.get(target - nums[i])
            if not pas is None:
                return [pas, i]
            prev[nums[i]] = i
        