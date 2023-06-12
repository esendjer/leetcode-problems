package two_sum

func twoSum(nums []int, target int) []int {
	prev := make(map[int]int)
	for i, v := range nums {
		res := target - v
		val, ok := prev[res]
		if ok {
			return []int{val, i}
		} else {
			prev[v] = i
		}
	}
	return []int{}
}