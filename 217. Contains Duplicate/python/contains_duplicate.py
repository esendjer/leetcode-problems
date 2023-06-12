from typing import List
import heapq

class Solution:
    def containsDuplicateH(self, nums: List[int]) -> bool:
        heapq.heapify(nums)
        p = heapq.heappop(nums)
        while nums:
            c = heapq.heappop(nums)
            if c == p:
                return True
            p = c
        return False

    def containsDuplicateS(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)

    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

cases = (
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2],
)

a = Solution()
b = a.containsDuplicateS

for i in cases:
    print(b(i))