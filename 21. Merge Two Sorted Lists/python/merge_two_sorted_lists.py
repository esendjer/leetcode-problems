from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ch1 = list1
        ch2 = list2
        fhs = ListNode(val=float("-inf"))
        fh = fhs
        sdf = 0
        while ch1 is not None or ch2 is not None:
            if not ch1 is None:
                if fh.val <= ch1.val:
                    if not (not ch2 is None and fh.val < ch1.val > ch2.val):
                        fh.next = ch1
                        fh = fh.next
                        ch1 = ch1.next
                else:
                    cc = ListNode(val=fh.val)
                    fh.val = ch1.val
                    fh.next = cc
                    fh = fh.next
                    ch1 = ch1.next
            if not ch2 is None:
                if fh.val <= ch2.val:
                    if not (not ch1 is None and fh.val < ch2.val > ch1.val):
                        fh.next = ch2
                        fh = fh.next
                        ch2 = ch2.next
                else:
                    cc = ListNode(val=fh.val)
                    fh.val = ch2.val
                    fh.next = cc
                    fh = fh.next
                    ch2 = ch2.next
        return fhs.next



cases = (
    ([1,2,4], [1,3,4]),
    ([], []),
    ([], [0]),
    ([5], [1,2,4]),
    ([-9,3], [5,7]),
    ([-2,5], [-9,-6,-3,-1,1,6]),
)

a = Solution()
b = a.mergeTwoLists

for i in cases:
    dl = []
    fl = ListNode() if i[0] else None
    sl = ListNode() if i[1] else None
    ll = fl
    for j in range(len(i[0])):
        ll.val = i[0][j]
        if j != len(i[0]) - 1:
            ll.next = ListNode()
            ll = ll.next
    tl = sl
    for j in range(len(i[1])):
        tl.val = i[1][j]
        if j != len(i[1]) - 1:
            tl.next = ListNode()
            tl = tl.next
    nl = b(fl, sl)
    while not nl is None:
        dl.append(nl.val)
        nl = nl.next
    print(dl)