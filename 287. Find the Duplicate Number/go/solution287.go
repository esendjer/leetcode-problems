package solution287

func findDuplicate(nums []int) int {
	b := make(map[int]int)
	mc := 0
	mv := 0
	for _, num := range nums {
		b[num] += 1
		if mc < b[num] {
			mc = b[num]
			mv = num
		}
	}
	return mv
}
