from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        n = ListNode(next=head)
        ch = n
        while not ch is None and not ch.next is None:
            if ch.next.val == val:
                ch.next = ch.next.next
            else:
                ch = ch.next
        return n.next

cases = (
    ([1,2,6,3,4,5,6], 6),
    ([],1),
    ([7,7,7,7], 7),
)

a = Solution()
b = a.removeElements

for i in cases:
    dl = []
    fl = ListNode() if i[0] else None
    ll = fl
    for j in range(len(i[0])):
        ll.val = i[0][j]
        if j != len(i[0]) - 1:
            ll.next = ListNode()
            ll = ll.next
    nl = b(fl, i[1])
    while not nl is None:
        dl.append(nl.val)
        nl = nl.next
    print(dl)