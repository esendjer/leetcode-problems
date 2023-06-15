from typing import List


class Solution:
    def longestConsecutiveS(self, nums: List[int]) -> int:
        d = set(nums)
        count = 0
        for i in nums:
            if not i-1 in d:
                t = 1
                while i+t in d:
                    t += 1
                count = max(count, t)
        return count

    def longestConsecutiveD(self, nums: List[int]) -> int:
        d = {i: True for i in nums}
        count = 0
        for i in nums:
            r = d.get(i - 1, False)
            if not r:
                t = 1
                while d.get(i + t, False):
                    t += 1
                count = max(count, t)
        return count