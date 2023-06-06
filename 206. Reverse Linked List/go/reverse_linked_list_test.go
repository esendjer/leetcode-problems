package reverseLinkedList

import (
	"reflect"
	"testing"
)

var Cases = [][]int{
	{1, 2, 3, 4, 5},
	{1, 2},
	{},
}
var Results = [][]int{
	{5, 4, 3, 2, 1},
	{2, 1},
	{},
}

func SimpleListToLL(a *[]int) *ListNode {
	ca := *a
	var fl *ListNode
	ll := &ListNode{}
	if len(ca) > 0 {
		fl = ll
	}
	for v := range ca {
		ll.Val = ca[v]
		if v != len(ca)-1 {
			ll.Next = &ListNode{}
			ll = ll.Next
		}
	}
	return fl
}

func LLToSimpleList(ll *ListNode) *[]int {
	dl := []int{}
	nl := ll
	for nl != nil {
		dl = append(dl, nl.Val)
		nl = nl.Next
	}
	return &dl
}

func TestSolution(t *testing.T) {
	for i := range Cases {
		fl := SimpleListToLL(&Cases[i])
		nl := reverseList(fl)
		dl := *LLToSimpleList(nl)
		// test
		want := Results[i]
		if !reflect.DeepEqual(dl, want) {
			t.Errorf("got %v, wanted %v", dl, want)
		}
	}
}

func TestSolutionOne(t *testing.T) {
	for i := range Cases {
		fl := SimpleListToLL(&Cases[i])
		nl := reverseListOne(fl)
		dl := *LLToSimpleList(nl)
		// test
		want := Results[i]
		if !reflect.DeepEqual(dl, want) {
			t.Errorf("got %v, wanted %v", dl, want)
		}
	}
}
