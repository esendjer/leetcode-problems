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
        d = a.reverseListS
        for i, v in enumerate(CASES):
            bl = []
            dl = []
            fl = ListNode() if v else None
            ll = fl
            for j in range(len(v)):
                ll.val = v[j]
                if j != len(v) - 1:
                    ll.next = ListNode()
                    ll = ll.next
            nb = b(fl)
            nd = d(fl)
            while not nb is None:
                bl.append(nb.val)
                nb = nb.next
            while not nd is None:
                dl.append(nd.val)
                nd = nd.next
            self.assertEqual(bl, RESULTS[i])
            self.assertEqual(dl, RESULTS[i])