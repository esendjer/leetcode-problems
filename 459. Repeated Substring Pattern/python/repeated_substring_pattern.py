class Solution:
    def repeatedSubstringPatternS(self, s: str) -> bool:
        return s in f"{s[1:]}{s[:-1]}"
    
    def repeatedSubstringPatternF(self, s: str) -> bool:
        ls = ""
        l = 0
        r = len(s)-1
        while l<r:
            ls = ls + s[l]
            if not len(s) % len(ls) and s.count(ls) * len(ls) == len(s):
                return True
            l+=1
            r-=1
        return False
