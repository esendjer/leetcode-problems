class Solution:
    def isPalindromeF(self, s: str) -> bool:
        a = "".join([i.lower() for i in s if i.isalnum()])
        return a == a[-1::-1]

    def isPalindromeS(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True