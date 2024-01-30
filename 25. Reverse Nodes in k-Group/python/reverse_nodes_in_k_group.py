from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge cases with empty and single-item list
        if not head or not head.next:
            return head
        dummy = ListNode(val=0, next=head)
        tmp_ll = dummy
        pre_n = dummy
        curr_n = head
        go_on = True
        while go_on:
            for _ in range(k-1):
                next_n = curr_n.next
                curr_n.next = next_n.next
                next_n.next = pre_n.next
                pre_n.next = next_n
            pre_n = curr_n
            curr_n = curr_n.next
            tmp_curr_n = curr_n
            for _ in range(k):
                if not tmp_curr_n:
                    go_on = False
                    break
                tmp_curr_n = tmp_curr_n.next
        return tmp_ll.next
                 
        