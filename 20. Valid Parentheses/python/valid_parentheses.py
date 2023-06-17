class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        o_s = []
        c_t = (")", "]", "}")
        d = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for i in s:
            if i in c_t:
                if len(o_s) != 0:
                    co = o_s.pop()
                    if i != d[co]:
                        return False
                else:
                    return False
            else:
                o_s.append(i)
        if len(o_s) !=0 :
            return False
        return True