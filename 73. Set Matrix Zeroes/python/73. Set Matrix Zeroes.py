from typing import List

class Solution:
    def setZeroesS(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        zr = 1  # int where in binary format is stored a row of 0
        # 1 in the beginning is needed to perform increasing rows which is not 0-filled
        # like, 0b1001 should be understood as 1_001, where 0 and 1 indexes are not 0-filled, but 2 index is
        zt = 0  # int where in binary format is stored columns of 0
        # but in this case there is need to perform Bitwise OR for collecting all the columns
        # in a very single line, so that, below _tzt_ variable is a temporary place for the current column
        # where 0 indexes are reflected and after _tzt_ is compared with _zt_ with Bin OR and 
        # then the result of comparison is stored in _zt_
        while i <= m -1:
            zr <<= 1
            tzt = 1
            j = 0
            while j <= n -1:
                tzt <<= 1
                if matrix[i][j] == 0:
                    if not zr & 1:
                       zr += 1
                    if not tzt & 1:
                        tzt += 1
                j += 1
            i += 1
            zt = zt | tzt
        i = m -1
        while zr > 1:
            j = n - 1
            if zr & 1:
                matrix[i] = [0] * n
            else:
                tzt = zt
                while tzt > 1:
                    if tzt & 1:
                        matrix[i][j] = 0
                    j -= 1   
                    tzt >>= 1                     
            zr >>= 1
            i -= 1
    
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
b = a.setZeroesS

for i in cases:
    b(i)
    print(i)