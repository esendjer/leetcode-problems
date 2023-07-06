class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows+1):
            a = []
            for j in range(i):
                if j == 0 or j == i-1:
                    a.append(1)
                else:
                    a.append(ans[-1][j-1] + ans[-1][j])
            ans.append(a)
        return ans