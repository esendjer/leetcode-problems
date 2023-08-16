from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  # current index
        c = 0  # count of repetition
        t = 1  # length without duplicates
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                if c:
                    nums[i:len(nums)] = nums[i+1:len(nums)]
                else:
                    i+=1
                    c+=1
                    t+=1
            else:
                i+=1
                c = 0
                t+=1
        return t