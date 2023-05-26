class Solution:
    def findMinBS(self, nums):
        """
        [3,4,5,1,2],
        [4,5,6,7,0,1,2],
        [11,13,15,17],
        [5,1,2,3,4],
        """
        ans = float("inf")
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < ans:
                ans = nums[m]
            if  nums[l] > nums[m]:
                if nums[m] < nums[r] and nums[r] < nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] > nums[r] and nums[r] < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
        return ans

    def findMin(self, nums) -> int:
        n_len = len(nums)
        left = 0
        right = n_len - 1
        for _ in range(n_len // 2):
            if nums[left] > nums[left + 1]:
                return nums[left + 1]
            if nums[right] < nums[right - 1]:
                return nums[right]
            left += 1
            right -=1
        return nums[0]

    def findMinPyNative(self, nums) -> int:
        # using Python native methods and functions
        return min(nums)

cases = (
    [3,4,5,1,2],
    [4,5,6,7,0,1,2],
    [11,13,15,17],
    [1],
    [1,2],
    [5,1,2,3,4],
)

a = Solution()
b = a.findMinBS

for i in cases:
    print(b(i))