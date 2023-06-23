from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i,v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and v == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                ts = v + nums[l] + nums[r]
                if ts == 0:
                    ta = [v, nums[l], nums[r]]
                    l += 1
                    if not (ans and ans[-1] == ta):
                        ans.append(ta)
                else:
                    if ts < 0:
                        l += 1
                    else:
                        r -= 1
        return ans


cases = (
    [-1,0,1,2,-1,-4],
    [0,1,1],
    [0,0,0],
    [-1,0,1,2,-1,-4,-2,-3,3,0,4],
)

a = Solution()
b = a.threeSum

for i in cases:
    print(b(i))