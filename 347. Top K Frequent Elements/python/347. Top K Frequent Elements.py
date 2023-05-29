from heapq import nlargest
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        return sorted(set(nums), key=lambda x: nums.count(x), reverse=True)[0:k]

    def topKFrequentHeap(self, nums, k):
        if k == len(nums):
            return nums
        count = Counter(nums)   # Counter type
        return nlargest(k, count.keys(), key=count.get) # heapq


cases = (
    ([1,1,1,2,2,3], 2),
    ([1], 1),
    ([1,2], 2),
)

a = Solution()
b = a.topKFrequentHeap


for i in cases:
    print(b(*i))