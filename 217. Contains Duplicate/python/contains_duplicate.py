from typing import List


class Solution:
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