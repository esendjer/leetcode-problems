

def lengthOfLongestSubstring(s: str) -> int:
    p_s = ""
    c_s = ""
    for i in s:
        if not i in c_s:
            c_s += i
        else:
            if len(p_s) < len(c_s):
                p_s = c_s
            c_s = c_s[c_s.index(i)+1:] + i
    return max(len(p_s), len(c_s))

a = (
    "abcabcbb", # 3
    "bbbbb",    # 1
    "pwwkew",   # 3
    " ",        # 1
    "dvdf",     # 3
)

for i in a:
    print(lengthOfLongestSubstring(i))