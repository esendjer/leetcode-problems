from typing import List
# Combination - https://en.wikipedia.org/wiki/Combination
# nCr(n, k) or C(n,k)  = n! / ((n-k)! * k!)
# Combinations work, but tooooooooooooooooooo much slowly
# For instance, the last test case has two 50-items lists (n=50) and k = 42
# 
# This solution is explained well in the video - https://www.youtube.com/watch?v=ax1DKi5lJwk
# 
# This problem also is a very similar to another one - 1383. Maximum Performance of a Team
import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        r = {k:v for k,v in enumerate(nums2)}
        g = sorted(r, key=r.get, reverse=True)
        f = 0
        res = 0
        h = []
        for i in g:
            f += nums1[i]
            heapq.heappush(h, nums1[i])
            if len(h) > k:
                f -= heapq.heappop(h)
            if len(h) == k:
                res = max(res, f * nums2[i])
        return res


cases = (
    ([1,3,3,2], [2,1,3,3], 3),
    ([4,2,3,1,1], [7,5,10,9,6], 1),
    ([2,1,14,12], [11,7,13,6], 3),
    (
        [93,463,179,2488,619,2006,1561,137,53,1765,2304,1459,1768,450,1938,2054,466,331,670,1830,1550,1534,2164,1280,2277,2312,1509,867,2223,1482,2379,1032,359,1746,966,232,67,1203,2474,944,1740,1775,1799,1156,1982,1416,511,1167,1334,2344],
        [345,229,976,2086,567,726,1640,2451,1829,77,1631,306,2032,2497,551,2005,2009,1855,1685,729,2498,2204,588,474,693,30,2051,1126,1293,1378,1693,1995,2188,1284,1414,1618,2005,1005,1890,30,895,155,526,682,2454,278,999,1417,1682,995],
        42
    ),
)

a = Solution()
b = a.maxScore

for i in cases:
    print(b(*i))