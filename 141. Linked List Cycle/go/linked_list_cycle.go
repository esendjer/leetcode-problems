package linked_list_cycle

// Definition for singly-linked list.
type ListNode struct {
	Val int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		if slow == fast.Next || slow.Next == fast.Next.Next {
			return true
		}
		slow = slow.Next
		fast = fast.Next.Next
		}
	return false
}