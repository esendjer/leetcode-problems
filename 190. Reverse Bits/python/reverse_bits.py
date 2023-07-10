class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)[2:]
        b = "".join(["0" for _ in range(32 - len(a))])
        return int((b+a)[-1::-1], base=2)
