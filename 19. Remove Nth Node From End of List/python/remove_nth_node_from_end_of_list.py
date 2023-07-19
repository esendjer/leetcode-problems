from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenLL = 0
        ch = head
        while ch:
            lenLL+=1
            ch = ch.next
        toDel = (lenLL - n) + 1
        cn = 1
        ch = head
        while ch:
            if cn == toDel - 1:
                ch.next = ch.next.next
                break
            if cn == toDel:
                head = ch.next
                break
            cn+=1
            ch = ch.next
        return head