from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ch = head
        while not ch is None and not ch.next is None:
            if ch.val == ch.next.val:
                ch.next = ch.next.next
            else:
                ch = ch.next
        return head

cases = (
    [1,1,2],
    [1,1,2,3,3],
    [],
    [1,1,1],
)

a = Solution()
b = a.deleteDuplicates

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