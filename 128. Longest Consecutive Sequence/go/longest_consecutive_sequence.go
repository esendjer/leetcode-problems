package main

func longestConsecutive(nums []int) int {
	d := make(map[int]bool)
	for _, i := range nums {
		d[i] = true
	}
	count := 0
	for _, n := range nums {
		_, ok := d[n-1]
		if !ok {
			t := 1
			for _, ex := d[n+t]; ex; {
				t += 1
				_, ex = d[n+t]
			}
			if t > count {
				count = t
			}
		}
	}
	return count
}

func main() {
	a := []int{100, 4, 200, 1, 3, 2}
	b := []int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}
	res := longestConsecutive(a)
	println(res)
	res = longestConsecutive(b)
	println(res)
}
