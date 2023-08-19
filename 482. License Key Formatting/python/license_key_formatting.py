class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ss = "".join([i for i in s.strip().split("-") if i]).upper()[::-1]
        a = ""
        for i in range(0,len(ss),k):
            end_i = i+k
            if end_i >= len(ss):
                end_i = len(ss)
            a += f"{ss[i:end_i]}-"
        return a[-2::-1]
