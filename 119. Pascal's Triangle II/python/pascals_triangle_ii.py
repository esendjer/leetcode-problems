class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(1, rowIndex+1):
            for j in range(1, i):
                ans[j-1] = ans[j-1] + ans[j]
            ans = [1] + ans
        return ans