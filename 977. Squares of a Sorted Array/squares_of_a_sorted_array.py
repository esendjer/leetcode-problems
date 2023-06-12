from typing import List


class Solution:
    def sortedSquaresT(self, nums: List[int]) -> List[int]:
        return sorted(n*n for n in nums)

    def sortedSquaresS(self, nums: List[int]) -> List[int]:
        resl = sorted(nums, key=abs)
        for i,v in enumerate(resl):
            resl[i] = (v)**2
        return resl

    def sortedSquaresF(self, nums: List[int]) -> List[int]:
        resl = []
        for i in nums:
            resl.append((i)**2)
        resl.sort()
        return resl