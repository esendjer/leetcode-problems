import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(dict)
        columns = collections.defaultdict(dict)
        box = collections.defaultdict(dict)
        for i, r in enumerate(board):
            for j, n in enumerate(r):
                if n.isdigit():
                    if rows[i].get(n, False):
                        return False
                    else:
                        rows[i][n] = True
                    if columns[j].get(n, False):
                        return False
                    else:
                        columns[j][n] = True
                    bi = (i // 3) * 10 + (j // 3)
                    if box[bi].get(n, False):
                        return False
                    else:
                        box[bi][n] = True
        return True

cases = (
    [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
    [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
)

a = Solution()
b = a.isValidSudoku

for i in cases:
    print(b(i))