class Solution:
    def mySqrt(self, x: int) -> int:
        c = 0
        d = 1 << 30
        while d > x:
            d >>= 2
        while d:
            if x >= c + d:
                x -= c + d
                c = (c >> 1) + d
            else:
                c >>= 1
            d >>= 2
        return c
