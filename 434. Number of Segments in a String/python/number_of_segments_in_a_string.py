class Solution:
    def countSegmentsF(self, s: str) -> int:
        return len(s.split())
    
    def countSegmentsS(self, s: str) -> int:
        a = 0
        for i in range(len(s)):
            if s[i] == " ":
                continue
            if (i>0 and s[i-1] == " ") or (a == 0 and s[i] != " "):
                a+=1
        return a