from typing import List


class Solution:
    def threeSumClosestS(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        diff = float("inf")
        for i,v in enumerate(nums):
            if i > 0 and nums[i] == [i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                ts = v + nums[l] + nums[r]
                if ts == target:
                    return target
                else:
                    c_diff = abs(target - ts)
                    if c_diff < diff:
                        diff = c_diff
                        ans = ts
                    if ts < target:
                        l += 1
                    else:
                        r -= 1
        return ans
        
    def threeSumClosestF(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = []
        for i,v in enumerate(nums):
            if i > 0 and nums[i] == [i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                ts = v + nums[l] + nums[r]
                if ts == target:
                    return target
                else:
                    ans.append(ts)
                    if ts < target:
                        l += 1
                    else:
                        r -= 1
        ans.sort()
        for i,v in enumerate(ans):
            if v>target and i>0:
                difi = max(ans[i-1], target) - min(ans[i-1], target)
                difv = max(v, target) - min(v, target)
                if difi <= difv:
                    return ans[i-1]
                else:
                    return v
        return ans[-1]