package add_two_numbers

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	ts := 0
	ch1 := l1
	ch2 := l2
	res := &ListNode{}
	ans := res
	for (ch1 != nil) || (ch2 != nil) || (ts != 0) {
		s1 := 0
		s2 := 0
		if ch1 != nil {
			s1 = ch1.Val
			ch1 = ch1.Next
		}
		if ch2 != nil {
			s2 = ch2.Val
			ch2 = ch2.Next
		}
		ts = ts + s1 + s2
		nn := ListNode{}
		if ts/10 != 0 {
			nn.Val = ts % 10
		} else {
			nn.Val = ts
		}
		ts = ts / 10
		res.Next = &nn
		res = res.Next
	}
	return ans.Next
}
