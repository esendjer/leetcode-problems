from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fr = "qwertyuiop"
        sr = "asdfghjkl"
        # tr = "zxcvbnm"
        a = []
        for w in words:
            rows = set()
            for c in set(w.lower()):
                if c in fr:
                    rows.add(1)
                elif c in sr:
                    rows.add(2)
                else:
                    rows.add(3)
                if len(rows) > 1:
                    break
            if len(rows) <= 1:
                a.append(w)
        return a