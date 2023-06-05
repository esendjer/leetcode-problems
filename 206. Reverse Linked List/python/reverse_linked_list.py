from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ch = head
        resNodes = None
        while ch is not None:
            resNodes = ListNode(val=ch.val, next=resNodes)
            ch = ch.next
        return resNodes


cases = (
    [1,2,3,4,5],
    [1,2],
    [],
)

a = Solution()
b = a.reverseList


for i in cases:
    dl = []
    fl = ListNode() if i else None
    ll = fl
    for j in range(len(i)):
        ll.val = i[j]
        if j != len(i) - 1:
            ll.next = ListNode()
            ll = ll.next
    nl = b(fl)
    while not nl is None:
        dl.append(nl.val)
        nl = nl.next
    print(dl)