package reverseLinkedList

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseListOne(head *ListNode) *ListNode {
	ch := head
	var resNodes *ListNode
	for ch != nil {
		tmpCh := ch.Next
		ch.Next = resNodes
		resNodes = ch
		ch = tmpCh
	}
	return resNodes
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
