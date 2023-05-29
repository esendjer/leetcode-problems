class Solution:
    def findDuplicate(self, nums) -> int:
        if len(nums) - len(set(nums)) == 1:
            return sum(nums) - sum(range(1, len(nums)))
        a = {nums.count(nums[0]): nums[0]}
        b = len(nums) // 2
        c = len(nums) % 2
        for i in range(1, b+1):
            a[nums.count(nums[i])] = nums[i]
            a[nums.count(nums[-i])] = nums[-i]
            if i == b and c:
                a[nums.count(nums[i+1])] = nums[i+1]
        return a[max(a)]
