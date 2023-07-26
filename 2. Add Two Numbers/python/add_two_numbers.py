# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbersT(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ch1 = l1
        ch2 = l2
        rem = 0
        ans = ListNode()
        pans = ans
        while ch1 or ch2 or rem > 0:
            f = 0
            s = 0
            if ch1:
                f = ch1.val
                ch1 = ch1.next
            if ch2:
                s = ch2.val
                ch2 = ch2.next
            r = f + s + rem
            rem = r // 10
            r = r % 10
            p = ListNode(
                val=r
            )
            pans.next = p
            pans = p
        return ans.next
    
    def addTwoNumbersS(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ts = 0
        ch2 = l2
        ch1 = l1
        ans = res = ListNode()
        while ch1 or ch2 or ts:
            s1 = 0
            s2 = 0
            if ch1:
                s1 = ch1.val
                ch1 = ch1.next
            if ch2:
                s2 = ch2.val
                ch2 = ch2.next
            ts = ts + s1 + s2
            if ts // 10:
                nn = ListNode(val=ts % 10)
            else:
                nn = ListNode(val=ts)
            res.next = nn
            res = res.next
            ts = ts // 10
        return ans.next
    
    def addTwoNumbersF(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        ch1 = l1
        s2 = ""
        ch2 = l2
        while ch1 or ch2:
            if ch1:
                s1 = f"{s1}{ch1.val}"
                ch1 = ch1.next
            else:
                s1 = f"{s1}0"
            if ch2:
                s2 = f"{s2}{ch2.val}"
                ch2 = ch2.next
            else:
                s2 = f"{s2}0"
        ts = int(s1[::-1]) + int(s2[::-1])
        res = ListNode()
        ans = res
        print(ts)
        while ts > 0:
            res.val = ts % 10
            ts //= 10
            if ts > 0:
                res.next = ListNode()
                res = res.next
        return ans