from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        s = ""
        e = ""
        for i,v in enumerate(nums):
            if not s:
                s = f"{v}"
            if i > 0 and (nums[i-1] == v-1 or nums[i-1] == v):
                e = f"{v}"
            elif i > 0 and nums[i-1] < v-1:
                if s == e or not e:
                    ans.append(s)
                else:
                    ans.append(f"{s}->{e}")
                s = f"{v}"
                e = s
        else:
            if not s:
                return ans
            if s == e or not e:
                ans.append(s)
            else:
                ans.append(f"{s}->{e}")
        return ans
