class Solution:
    def isAnagramH(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs = 0
        ht = 0
        for i, v in enumerate(s):
            hs += hash(v)
            ht += hash(t[i])
        return ht == hs

    def isAnagramSP(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = 0
        ts = 0
        sp = 1
        tp = 1
        for i, v in enumerate(s):
            ss += ord(v)
            ts += ord(t[i])
            sp *= ord(v)
            tp *= ord(t[i])
        return ss == ts and sp == tp
    
    def isAnagramD(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        for i in range(len(s)):
            ds[s[i]] = ds.get(s[i], 0) + 1
            dt[t[i]] = dt.get(t[i], 0) + 1
        return ds == dt
    
    def isAnagramS(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = sorted(s, key=ord)
        b = sorted(t, key=ord)
        for i, v in enumerate(a):
            if v != b[i]:
                return False
        return True