from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        c_s = ""

        def backtrack(o_p, c_p):
            nonlocal c_s
            if c_p == o_p == n:
                ans.append(c_s)
                return
            if o_p < n:
                c_s = c_s + "("
                backtrack(o_p+1, c_p)
                c_s = c_s[:len(c_s)-1]
            if c_p < o_p:
                c_s = c_s + ")"
                backtrack(o_p, c_p+1)
                c_s = c_s[:len(c_s)-1]
        backtrack(0,0)
        return ans