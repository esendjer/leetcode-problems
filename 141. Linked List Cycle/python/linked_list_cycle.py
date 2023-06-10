# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow
        while fast and fast.next:
            if slow is fast.next or \
                slow.next is fast.next.next:
                return True
            slow = slow.next
            fast = fast.next.next
        return False