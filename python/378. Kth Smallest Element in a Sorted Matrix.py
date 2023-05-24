class Solution:
    def kthSmallestHeap(self, matrix, k):
        from heapq import merge as heap_merge
        m_heap = heap_merge(*matrix)
        for _ in range(k):
            val = next(m_heap)
        return val

    def kthSmallest(self, matrix, k):
        a = [j for i in matrix for j in i]
        a.sort()
        return a[k-1]


cases = (
    ([[1,5,9],[10,11,13],[12,13,15]], 8),
    ([[-5]], 1),
    ([[1,2],[1,3]], 1),
    ([[1,3,5],[6,7,12],[11,14,14]], 1),
    ([[1,2],[1,3]], 3),
    ([[1,2],[1,3]], 4),
    ([[1,3,5],[6,7,12],[11,14,14]], 6)
)

a = Solution()
b = a.kthSmallestHeap

for i in cases:
    print(b(*i))



# {1, 5, 9, 10, 11, 12, 13, 15} 7
# [1, 5, 9, 10, 11, 12, 13, 13, 15]