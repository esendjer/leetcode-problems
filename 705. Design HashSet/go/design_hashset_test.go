package designHashSet

import "testing"

func TestSolution(t *testing.T) {
	// ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
	// [[],         [1],  [2],  [1],       [3],       [2],  [2],       [2],      [2]]
	a := Constructor()
	a.Add(1)
	a.Add(2)
	res := a.Contains(1)
	if !res {
		t.Errorf("got %t, wanted %t", res, true)
	}
	res = a.Contains(3)
	if res {
		t.Errorf("got %t, wanted %t", res, false)
	}
	a.Add(2)
	res = a.Contains(2)
	if !res {
		t.Errorf("got %t, wanted %t", res, true)
	}
	a.Remove(2)
	res = a.Contains(2)
	if res {
		t.Errorf("got %t, wanted %t", res, false)
	}
	//  * obj := Constructor();
	// * obj.Add(key);
	// * obj.Remove(key);
	// * param_3 := obj.Contains(key);
}
