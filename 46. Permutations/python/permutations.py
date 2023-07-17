class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        ans = []
        for _ in range(len(nums)):
            n = nums.pop(0)
            res = self.permute(nums)
            for j in res:
                j.append(n)
            ans.extend(res)
            nums.append(n)
        return ans