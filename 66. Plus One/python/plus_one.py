class Solution:
    def plusOneS(self, digits: List[int]) -> List[int]:
        d = 0
        p = 1
        dl = len(digits)
        for i in range(dl-1,-1,-1):
            d = d + digits[i] * p
            if i == dl-1:
                p = 10
            else:
                p *=10
        d = d + 1
        i=dl-1
        while d:
            c = d % 10
            d = d // 10
            if i >= 0:
                digits[i] = c
                i-=1
            else:
                digits = [c] + digits
        return digits

    def plusOneF(self, digits: List[int]) -> List[int]:
        d = 0
        p = 1
        dl = len(digits)
        for i in range(dl-1,-1,-1):
            d = d + digits[i] * p
            if i == dl-1:
                p = 10
            else:
                p *=10
        d = d + 1
        ans = []
        while d:
            c = d % 10
            d = d // 10
            ans.append(c)
        return ans[-1::-1]