class Solution:
    def findMin(self, nums) -> int:
        # searching in two directions
        # from the beginning to middle
        # and
        # from the end to to middle as well
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
    [1,2]
)