class Solution:
    def lengthOfLastWordT(self, s: str) -> int:
        r = len(s) -1
        a = 0
        while r >= 0:
            if s[r] != " ":
                a +=1
            else:
                if a > 0:
                    return a
            r -=1
        return a
    
    def lengthOfLastWordF(self, s: str) -> int:
        a = 0
        for i,v in enumerate(s):
            if v != " ":
                if i > 0 and s[i-1] == " ":
                    a = 0
                a += 1
        return a

    def lengthOfLastWordS(self, s: str) -> int:
        return len(s.split()[-1])
