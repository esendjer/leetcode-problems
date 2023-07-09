from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d = {}
        ch1 = headA
        ch2 = headB
        while ch1 or ch2:
            if ch1:
                dv1 = d.get(ch1.val)
                if dv1 and dv1 is ch1:
                    return ch1
                d[ch1.val] = ch1
                ch1 = ch1.next
            if ch2:
                dv2 = d.get(ch2.val)
                if dv2 and dv2 is ch2:
                    return ch2
                d[ch2.val] = ch2
                ch2 = ch2.next
