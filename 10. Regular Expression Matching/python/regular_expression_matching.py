import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        d = re.search(r'{}'.format(p), s)
        if d and len(s) == len(range(*d.span())):
            return True
        return False

cases = (
    ("aa", "a"),
    ("aa", "a*"),
    ("ab", ".*"),
    ("ab", ".*c"),
)

results = (
    False,
    True,
    True,
    False,
)

a = Solution()
b = a.isMatch

for i,v in enumerate(cases):
    res = b(*v)
    if res == results[i]:
        print(f"Correct: for case {i+1} {v}, result is {res}")
    else:
        print(f"Incorrect: for case {i+1} {v}, result should be {results[i]}")