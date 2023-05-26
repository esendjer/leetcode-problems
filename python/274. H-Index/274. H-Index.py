from typing import List

import heapq
class Solution:
    def hIndexW(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i = 0
        ic = 0
        while i <= len(citations) -1:
            if citations[i] > ic:
                ic += 1
            if citations[i] <= ic:
                return ic
            i += 1
        return ic
    
    def hIndex(self, citations: List[int]) -> int:
        heapq.heapify(citations)
        while True:
            a = heapq.heappop(citations)
            if a > len(citations):
                return len(citations) + 1
            if a == len(citations):
                return len(citations)
            if len(citations) <= 0:
                return 0

cases = (
    [3,0,6,1,5],
    [1,3,1],
    [100],
    [0,1],
    [2,1,2,6,1,8,10,10],
)

a = Solution()
b = a.hIndexW

for i in cases:
    print(b(i))