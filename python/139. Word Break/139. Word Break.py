# 
# 
# NOT SOLVED
# 
# 
;
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        words = []
        for i in range(len(wordDict)):
            for j in range(len(wordDict)):
                words.append(wordDict[i]+wordDict[j])
        for i in words:
            if i in s:
                if len(i) == len(s):
                    return True
                suf = s.index(i) + len(i)
                if suf < len(s) and s[suf:] in wordDict:
                    return True
        return False


cases = (
    ("leetcode", ["leet","code"]),
    ("applepenapple", ["apple","pen"]),
    ("catsandog", ["cats","dog","sand","and","cat"]),
    ("bb", ["a","b","bbb","bbbb"]),
    ("a",["a"]),
    ("apple", ["pear","apple","peach"]),
)

a = Solution()
b = a.wordBreak

for i in cases:
    print(b(*i))