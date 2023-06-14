from heapq import nlargest
from collections import Counter
from typing import List

class Solution:
    def topKFrequentD(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return [i for i in sorted(d, key=d.get, reverse=True)[0:k]]
    
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