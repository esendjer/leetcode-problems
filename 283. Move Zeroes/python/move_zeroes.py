from typing import List


class Solution:
    def moveZeroesM(self, nums: List[int]) -> None:
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                nums.append(nums.pop(i))

    def moveZeroesP(self, nums: List[int]) -> None:
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1