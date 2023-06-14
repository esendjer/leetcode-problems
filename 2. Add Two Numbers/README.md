# 2. Add Two Numbers

[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

Could be done within a very one while loop
```python
...
dummy = ListNode(0)
curr = dummy 
carry = 0

while l1 or l2 or carry:
    num1 = l1.val if l1 else 0
    num2 = l2.val if l2 else 0
    val = num1 + num2 + carry
    carry = val // 10
    val = val % 10 
    node = ListNode(val)
    curr.next = node 
    curr = curr.next
    l1 = l1.next if l1 else 0
    l2 = l2.next if l2 else 0

return dummy.next
```