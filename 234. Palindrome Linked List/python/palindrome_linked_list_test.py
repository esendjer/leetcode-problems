import unittest

from palindrome_linked_list import (
    Solution,
    ListNode,
)

from cases import cases

RESULTS = (
    True,
    False,
    True,
    True,
    True,
    True,
    False,
    False,
    True,
)

class TestSolution(unittest.TestCase):
    def runTest(self):
        a = Solution()
        b = a.isPalindromeD
        for i, v in enumerate(cases):
            dl = []
            fl = ListNode() if v else None
            ll = fl
            for j in range(len(v)):
                ll.val = v[j]
                if j != len(v) - 1:
                    ll.next = ListNode()
                    ll = ll.next
            res = b(fl)
            self.assertEqual(res, RESULTS[i])