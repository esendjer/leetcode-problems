from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindromeD(self, head: Optional[ListNode]) -> bool:
        # count length of the list
        l = 0
        ch = head
        while not ch is None:
            l += 1
            ch = ch.next
        last = l

        # divide the list in two
        ch2 = head
        for i in range(last // 2):
            ch2 = ch2.next
        
        # reverse the second part
        pre = None
        while ch2 is not None:
            tmp_ch = ch2.next
            ch2.next = pre
            pre = ch2
            ch2 = tmp_ch
        
        # compare both parts
        ch1 = head
        while pre is not None:
            if pre.val != ch1.val:
                return False
            pre = pre.next
            ch1 = ch1.next
        return True
    
    def isPalindromeS(self, head: Optional[ListNode]) -> bool:
        l = []
        ch = head
        while not ch is None:
            l.append(ch.val)
            ch = ch.next
        while len(l) > 1:
            if l.pop() != l.pop(0):
                return False
        return True

    def isPalindromeN(self, head: Optional[ListNode]) -> bool:
        # Works but really slow
        n = 1
        ch = head
        while not ch is None:
            n *= 10
            n += ch.val
            ch = ch.next
        else:
            n = n * 10 + 1
        revers = 0
        s = n
        while s != 0:
            revers = (revers * 10) + (s % 10)
            s //= 10
        return revers == n
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ""
        ch = head
        while not ch is None:
            s += str(ch.val)
            ch = ch.next
        return s == s[-1::-1]
