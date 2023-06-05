import unittest

from reverse_linked_list import (
    Solution,
    ListNode,
)

RESULTS = (
	[5, 4, 3, 2, 1],
	[2, 1],
	[],
)

CASES = (
    [1,2,3,4,5],
    [1,2],
    [],
)

class TestSolution(unittest.TestCase):
    def runTest(self):
        a = Solution()
        b = a.reverseList
        for i, v in enumerate(CASES):
            dl = []
            fl = ListNode() if v else None
            ll = fl
            for j in range(len(v)):
                ll.val = v[j]
                if j != len(v) - 1:
                    ll.next = ListNode()
                    ll = ll.next
            nl = b(fl)
            while not nl is None:
                dl.append(nl.val)
                nl = nl.next
            self.assertEqual(dl, RESULTS[i])