
from typing import List


class Solution:
    def findDuplicatesP(self, nums: List[int]) -> List[int]:
        f = []
        ai = len(nums) - 1
        for i in range(len(nums)):
            ci = abs(nums[i]) - 1
            if ci > ai:
                continue
            if nums[ci] > 0:
                nums[ci] = -nums[ci]
            else:
                f.append(abs(nums[i]))
        return f
    
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = [0] * n
        for i in range(n):
            s_i = nums[i] - 1 # all the integers of nums are in the range [1, n] 
            s[s_i] += 1
        return [i + 1 for i,v in enumerate(s) if v > 0]

cases = (
    [4,3,2,7,8,2,3,1],
    [1,1,2],
    [1],
    [1,1],
    [2,2]
)

a = Solution()
b = a.findDuplicatesP

for i in cases:
    print(b(i))