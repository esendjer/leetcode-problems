class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a = []
        s = n
        ans = -1
        j = 0
        while True:
            f = n % s
            if not f:
                a.append(s)
            s -= 1
            if s < 1:
                break
        if len(a) < k:
            return ans
        for _ in range(1, k +1):
            ans = a.pop()
        return ans


cases =(
    (12, 3),
    (7,2),
    (4,4,),
    (1000, 3),
)

a = Solution()
b = a.kthFactor

for i in cases:
    print(b(*i))