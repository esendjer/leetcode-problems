from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                if abs(d[nums[i]] - i) <= k:
                    return True
                else:
                    d[nums[i]] = i
            else:
                d[nums[i]] = i
        return False