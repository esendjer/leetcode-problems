class Solution:
    def isHappy(self, n: int) -> bool:
        # if there is recursion then repeated results occur
        a = []
        while True:
            w = 0
            while n > 0:
                p = n % 10
                n = n // 10
                w = w + p**2
            n = w
            if n == 1:
                return True
            if n in a:
                return False
            a.append(n)
            if n > (2**31) - 1:
                break
        return False
