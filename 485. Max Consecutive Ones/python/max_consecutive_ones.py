class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        c = 0
        for n in nums:
            if n == 1:
                c += 1
            else:
                m = max(m,c)
                c = 0
        m = max(m,c)
        return m
    