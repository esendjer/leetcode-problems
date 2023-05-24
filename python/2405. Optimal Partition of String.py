# Stolen from https://github.com/doocs/leetcode/blob/main/solution/2400-2499/2405.Optimal%20Partition%20of%20String/README_EN.md
class Solution:
    def partitionString(self, s: str) -> int:
        ss = set()
        ans = 1
        for c in s:
            print(ss)
            if c in ss:
                ans += 1
                ss = set()
            ss.add(c)
        return ans


cases = (
    "abacaba",
    "ssssss"
)

a = Solution()
b = a.partitionString

for i in cases:
    print(b(i))