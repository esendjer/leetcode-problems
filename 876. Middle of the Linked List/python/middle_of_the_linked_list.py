
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNodeM(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def middleNodeM(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ch = head
        l_ch = 0
        while not ch is None:
            l_ch += 1
            ch = ch.next
        l_ch = l_ch // 2
        ch = head
        i = 0
        while i != l_ch:
            i += 1
            ch = ch.next
        return ch

