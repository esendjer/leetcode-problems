package reverseLinkedList

import (
	"reflect"
	"testing"
)

func TestSolution(t *testing.T) {
	cases := [][]int{
		{1, 2, 3, 4, 5},
		{1, 2},
		{},
	}
	results := [][]int{
		{5, 4, 3, 2, 1},
		{2, 1},
		{},
	}
	for i := range cases {
		dl := []int{}
		var fl *ListNode
		ll := &ListNode{}
		if len(cases[i]) > 0 {
			fl = ll
		}
		for v := range cases[i] {
			ll.Val = cases[i][v]
			if v != len(cases[i])-1 {
				ll.Next = &ListNode{}
				ll = ll.Next
			}
		}
		nl := reverseList(fl)
		for nl != nil {
			dl = append(dl, nl.Val)
			nl = nl.Next
		}
		// test
		want := results[i]
		if !reflect.DeepEqual(dl, want) {
			t.Errorf("got %v, wanted %v", dl, want)
		}
	}
}
