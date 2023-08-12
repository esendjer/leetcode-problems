class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y)[2:].count("1")
        # or return bin(x ^ y).count("1") is pretty much the same