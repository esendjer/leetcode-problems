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
    
    def countSegmentsT(self, s: str) -> int:
        a = 0
        l = len(s)
        for i in range(l):
            if s[i] == " " and i and s[i-1] != " ":
                a+=1
            if i==l-1 and s[i] != " ":
                a+=1
        return a