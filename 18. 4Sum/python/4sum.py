class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        a, b = [], []
        
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    b.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    b.pop()
                return
            l, r = start, len(nums)-1
            while l<r:
                if nums[l] + nums[r] == target:
                    t = b + [nums[l], nums[r]]
                    l += 1
                    if not (a and a[-1] == t):
                        a.append(t)
                else:
                    if nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
        kSum(4, 0, target)
        return a