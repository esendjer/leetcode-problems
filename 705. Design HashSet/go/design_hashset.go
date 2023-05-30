package designHashSet

type SimpleNode struct {
	Key  int
	Used bool
}

type MyHashSet struct {
	Set []SimpleNode
}

func Constructor() MyHashSet {
	return MyHashSet{
		Set: make([]SimpleNode, 1000001),
	}
}

func (mhs *MyHashSet) Add(key int) {
	mhs.Set[key] = SimpleNode{key, true}
}

func (mhs *MyHashSet) Remove(key int) {
	mhs.Set[key] = SimpleNode{}
}

func (mhs *MyHashSet) Contains(key int) bool {
	return mhs.Set[key].Used
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
