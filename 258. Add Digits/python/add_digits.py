class Solution:
    def addDigitsW(self, num: int) -> int:
        while True:
            w = 0
            while num > 0:
                p = num % 10
                num = num // 10
                w+=p
            num = w
            if not num // 10:
                return num
        return num
    
    def addDigitsM(self, num: int) -> int:
        return num%9 + (9 * (num%9 == 0 and num != 0))