from typing import List

class Solution:
    def searchBSClean(self, nums: List[int], target: int) -> int:
        l_i = 0
        r_i = len(nums) -1
        while r_i >= l_i:
            m_i = (r_i + l_i) // 2
            if nums[m_i] == target:
                return m_i
            if nums[l_i] > nums[m_i]:
                if nums[m_i] > target or target > nums[r_i]:
                    r_i = m_i - 1
                else:
                    l_i = m_i + 1
            else:
                if nums[m_i] < target or  target < nums[l_i]:
                    l_i = m_i + 1
                else:
                    r_i = m_i - 1
        return -1

    def searchBSCouples(self, nums: List[int], target: int) -> int:
        l_i = 0
        r_i = len(nums) -1
        while r_i >= l_i:
            m_i = (r_i + l_i) // 2
            print(l_i, m_i, r_i)
            if nums[m_i] == target:
                return m_i
            if nums[l_i] == target:
                return l_i
            if nums[r_i] == target:
                return r_i
            if nums[l_i] > nums[m_i]:
                if nums[m_i] > target or target > nums[r_i]:
                    r_i = m_i - 1
                    l_i += 1
                else:
                    r_i -= 1
                    l_i = m_i + 1
            else:
                if nums[m_i] < target or  target < nums[l_i]:
                    r_i -= 1
                    l_i = m_i + 1
                else:
                    r_i = m_i - 1
                    l_i += 1
        return -1

    def searchCouplesWhile(self, nums, target):
        len_n = len(nums)
        l_1 = 0
        l_2 = 1
        while True:
            if nums[l_1] == target:
                return l_1
            if l_2 <= len_n - 1:
                if nums[l_2] == target:
                    return l_2
            l_1 += 2
            l_2 += 2
            if l_1 > len_n - 1:
                return -1
    
    def searchCouplesFor(self, nums, target):
        len_n = len(nums)
        ans = -1
        for i in range(0, len_n, 2):
            if nums[i] == target:
                return i
            if i + 1 <= len_n -1 and nums[i+1] == target:
                return i + 1
        return ans

    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1


cases = (
    ([4,5,6,7,0,1,2], 0),
    ([4,5,6,7,0,1,2], 3),
    ([1], 0),
    ([7,8,1,2,3,4,5,6], 2),
    ([4,5,6,7,0,1,2], 6),
    ([4,5,6,7,8,9,1,2,3], 1),
    #         4 5     8
)

a = Solution()
b = a.searchBSClean

for i in cases:
    print(b(*i))
