from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sn = [None]
        sn[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                sn.append(nums[i])
        for i in range(len(nums)):
            if i < len(sn):
                nums[i] = sn[i]
            else:
                nums[i] = None
        return int(len(sn))

cases = (
    [1,1,2],
    [0,0,1,1,1,2,2,3,3,4]
)

a = Solution()
b = a.removeDuplicates

for i in cases:
    r = b(i)
    print(r, type(r))
    print(i)