def findMedianSortedArrays(nums1, nums2):
    fin_arr = []
    fin_arr.extend(nums1)
    fin_arr.extend(nums2)
    fin_arr.sort()
    fin_len = len(fin_arr)
    med_i = (fin_len - 1) // 2
    if fin_len % 2 != 0:
        return float(fin_arr[med_i])
    med_i1 = med_i + 1
    return (fin_arr[med_i] + fin_arr[med_i1]) / 2

cases = (
    ([1,3], [2]),
    ([1,2], [3,4]),
)

a = findMedianSortedArrays

for i in cases:
    print(a(*i))
