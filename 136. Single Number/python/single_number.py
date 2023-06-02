from typing import List
import heapq
class Solution:
    def singleNumberH(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        heapq.heapify(nums)
        while len(nums) >= 0:
            f0 = heapq.heappop(nums)
            if len(nums) == 0:
                return f0
            f1 = heapq.heappop(nums)
            if f0 != f1:
                return f0
    
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i-1]:
                return nums[i-1]
            if i == len(nums) - 2:
                return nums[i+1]


cases = (
    [2,2,1],
    [4,1,2,1,2],
    [1],
)

a = Solution()
b = a.singleNumberH

for i in cases:
    print(b(i))