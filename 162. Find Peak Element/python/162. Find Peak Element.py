from typing import List


class Solution:
    def findPeakElementBS(self, nums: List[int]) -> int:
        """
        [3,4,3,2,1]
        """
        ans_i = 0
        l = 0
        r = len(nums) -1
        while l <= r:
            m = (l + r) // 2
            if  nums[ans_i] < nums[m]:
                ans_i = m
            # right part is larger
            if nums[l] <= nums[m] < nums[r]:
                l = m + 1
            # left part is larger
            elif nums[l] > nums[m] >= nums[r]:
                r = m - 1
            # in cases when all of parts looks similar
            # just chang any thing possible
            else:
                r -= 1
        return ans_i

    def findPeakElement(self, nums: List[int]) -> int:
        len_n = len(nums)
        ans_i = 0
        for i in range(len_n // 2):
            if nums[i] > nums[ans_i]:
                ans_i = i
            if nums[-1 - i] > nums[ans_i]:
                ans_i = len_n - i -1
            if i == len_n // 2 - 1 and len_n % 2:
                if nums[-2 - i] > nums[ans_i]:
                    ans_i = len_n - i -2
        return ans_i
    
    def findPeakElementSecondWay(self, nums: List[int]) -> int:
        len_n = len(nums)
        ans_i = 0
        for i in range(0, len_n, 2):
            if nums[i] > nums[ans_i]:
                ans_i = i
            if i < len_n - 1 and nums[i+1] > nums[ans_i]:
                ans_i = i + 1
        return ans_i


cases = (
    [1,2,3,1],
    [1,2,1,3,5,6,4],
    [1,2,1],
    [1,2,2,3,1],
    [3,4,3,2,1],
    [1,2,3,4,3,2],
)

a = Solution()
b = a.findPeakElementBS

for i in cases:
    print(b(i))