package reverseLinkedList

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	ch := head
	var resNodes *ListNode
	for ch != nil {
		preRes := ListNode{Val: ch.Val, Next: resNodes}
		resNodes = &preRes
		ch = ch.Next
	}
	return resNodes
}
