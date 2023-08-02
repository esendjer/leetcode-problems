class Solution:
    def isPowerOfTwoT(self, n: int) -> bool:
        if n <= 0:
            return False
        d = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384)
        if n in d:
            return True
        else:
            c = 0
            i = 15
            while c < n and i <= 31:
                c = 2**i
                if c == n:
                    return True
                i+=1
        return False
    
    def isPowerOfTwoS(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            if n in [2**i for i in range(31)]:
                return True
        return False
    
    def isPowerOfTwoF(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            c = 0
            i = 0
            while c < n and i <= 31:
                c = 2**i
                if c == n:
                    return True
                i+=1
        return False
                    