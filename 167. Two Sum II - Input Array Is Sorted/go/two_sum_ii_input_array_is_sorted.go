package two_sum_ii_input_array_is_sorted

func twoSum(numbers []int, target int) []int {
    f := 0
    l := len(numbers) - 1
    for l > f {
        s := numbers[f] + numbers[l]
        if s == target {
            return []int{f+1, l+1}
        }
        if s < target {
            f += 1
        }
        if s > target {
            l -= 1
        }
    }
    return []int{}
}