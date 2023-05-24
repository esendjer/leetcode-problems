class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        # searching in two directions
        # from the beginning to middle
        # and
        # from the end to to middle as well
        left = 0
        right = len(arr) -1
        for _ in range(len(arr) // 2 + 1):
            if arr[left] > arr[left+1]:
                return left
            if arr[right] > arr[right-1]:
                return right
            left += 1
            right -= 1
        return arr.index(max(arr))

    def peakIndexInMountainArrayPyNative(self, arr) -> int:
        # using Python native methods and functions
        return arr.index(max(arr))


cases = (
    [0,1,0],
    [0,2,1,0],
    [0,10,5,2]
)