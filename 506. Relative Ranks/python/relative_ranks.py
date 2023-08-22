class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        r = [
            "Gold Medal",
            "Silver Medal",
            "Bronze Medal",
        ]
        d = {v:i for i,v in enumerate(score)}
        a = ["" for _ in range(len(score))]
        i = 0
        for k in sorted(d, reverse=True):
            if i > len(r)-1:
                a[d[k]] = f"{i+1}"
            else:
                a[d[k]] = r[i]
            i+=1
        return a
    