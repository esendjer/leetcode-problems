import unittest

from string_to_integer_atoi import (
    Solution,
)

RESULTS = (
	2147483647,
    42,
    -42,
    4193,
    32,
    0,
    2147483647,
    2147483647,
    2147483646,
    -2147483648,
    -2147483648,
    -2147483647,
)

CASES = (
    "91283472332",
    "42",
    "   -42",
    "4193 with words",
    "0032",
    "+-12",
    "2147483648",
    "2147483647",
    "2147483646",
    "-2147483649",
    "-2147483648",
    "-2147483647",
)

class TestSolution(unittest.TestCase):
    def runTest(self):
        a = Solution()
        b = a.myAtoi
        for i, v in enumerate(CASES):
            res = b(v)
            self.assertEqual(res, RESULTS[i])
