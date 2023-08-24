class Solution:
    def fibIter(self, n: int) -> int:
        if n in [0, 1]:
            return n
        c = 0
        pp = 0
        pn = 1
        while c < n:
            pp, pn = pn, pp + pn
            c+=1
        return pp

    def fibRecur(self, n: int) -> int:
        if n in [0, 1]:
            return n
        return self.fibRecur(n-1) + self.fibRecur(n-2)