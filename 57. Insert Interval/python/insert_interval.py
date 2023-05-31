from typing import List
import heapq

class Solution:
    def insertH(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        heapq.heapify(intervals)
        a = []
        while len(intervals) > 0:
            cur_i = heapq.heappop(intervals)
            if not a or a[-1][1] < cur_i[0]:
                a.append(cur_i)
            else:
                a[-1][1] = max(cur_i[1], a[-1][1])
        return a
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        a = []
        while len(intervals) > 0:
            cur_i = intervals.pop(0)
            if not a or a[-1][1] < cur_i[0]:
                a.append(cur_i)
            else:
                a[-1][1] = max(cur_i[1], a[-1][1])
        return a


cases = (
    ([[1,3],[6,9]], [2,5]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]),
)

a = Solution()
b = a.insertH

for i in cases:
    print(b(*i))