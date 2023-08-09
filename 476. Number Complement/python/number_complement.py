class Solution:
    def findComplement(self, num: int) -> int:
        b = "".join(["1" for _ in bin(num)[2:]])
        return int(b, base=2) ^ num
