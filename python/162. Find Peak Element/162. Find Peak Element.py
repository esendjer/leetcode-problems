from typing import List


class Solution:
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


cases = ([1,2,3,1], [1,2,1,3,5,6,4], [1,2,1])

a = Solution()
b = a.findPeakElementSecondWay

for i in cases:
    print(b(i))