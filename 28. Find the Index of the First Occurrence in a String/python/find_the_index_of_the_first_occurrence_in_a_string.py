class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i,v in enumerate(haystack):
            if v == needle[0]:
                l = i
                r = i + len(needle)
                if needle == haystack[l:r]:
                    return i
        return -1