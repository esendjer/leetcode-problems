from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListS(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ch = head
        resNodes = None
        while ch is not None:
            tmp_ch = ch.next
            ch.next = resNodes
            resNodes = ch
            ch = tmp_ch
        return resNodes
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ch = head
        resNodes = None
        while ch is not None:
            resNodes = ListNode(val=ch.val, next=resNodes)
            ch = ch.next
        return resNodes
