from itertools import (
    combinations,
    combinations_with_replacement,
)
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if not n or not k or maxPts * k < n:
            return 1.0
        answer = 0
        probs = [0] * (n+1)
        probs[0] = 1.0
        cur_value = probs[0]
        for i in range(1, n+1):
            probs[i] = cur_value / maxPts
            if i < k:
                cur_value += probs[i]
            else:
                answer += probs[i]
            if i - maxPts >= 0:
                cur_value -= probs[i - maxPts]
        return answer

cases = (
    (10, 1, 10),
    (6, 1, 10),
    (21, 17, 10),
    (0, 0, 1),
    (12, 1, 10)
)

a = Solution()
b = a.new21Game

for i in cases:
    print(b(*i))