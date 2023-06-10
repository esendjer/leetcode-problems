class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replacement = {}
        used = {}
        for i, c in enumerate(s):
            cur_c = replacement.get(c, "")
            if cur_c:
                if cur_c != t[i]:
                    return False
            else:
                if used.get(t[i], ""):
                    return False
                replacement[c] = t[i]
                used[t[i]] = True
        return True