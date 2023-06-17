from typing import List


class Solution:
    def twoSumB(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        l = len(numbers) - 1
        while l > f:
            s = numbers[f] + numbers[l]
            if s == target:
                return f+1, l+1
            if s > target:
                l -= 1
            if s < target:
                f += 1
    
    def twoSumD(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(numbers):
            r = d.get(target - v, None)
            if not r is None:
                return r + 1, i + 1
            d[v] = i
        