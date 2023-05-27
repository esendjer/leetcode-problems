from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        zr = 1
        while i <= m -1:
            zr <<= 1
            j = 0
            while j <= n -1:
                pre_i = i
                if i > 0:
                    pre_i = i - 1
                if matrix[i][j] == 0 and not zr & 1:
                    zr += 1
                if pre_i != i and matrix[pre_i][j] == 0:
                    matrix[i][j] = 0
                j += 1
            i += 1
        i = m -1
        while i >= 0:
            j = n -1
            while j >= 0:
                pre_i = i
                if i < m - 1:
                    pre_i = i + 1
                if pre_i != i and matrix[pre_i][j] == 0:
                    matrix[i][j] = 0
                j -= 1
            i -= 1
        i = m -1
        while zr > 1:
            if zr & 1:
                j = 0
                while j <= n - 1:
                    matrix[i][j] = 0
                    j += 1
            zr >>= 1
            i -= 1


cases = (
    [[1,1,1],[1,0,1],[1,1,1]],
    [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
    [[1,3,1,5], [3,4,5,2], [0,1,2,0]],
    [[1]],
    [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]],
)

a = Solution()
b = a.setZeroes

for i in cases:
    b(i)
    print(i)