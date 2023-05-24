def missingNumber(nums):
    max_n = len(nums)
    a = sum(set(range(max_n + 1))) - sum(nums)
    return a



cases = ([3,0,1], [0,1], [9,6,4,2,3,5,7,0,1])

for i in cases:
    print(missingNumber(i))