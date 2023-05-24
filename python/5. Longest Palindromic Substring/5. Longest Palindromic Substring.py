def longestPalindrome(s):
    if s == s[-1::-1]:
        return s
    polind_sub_str = s[0]
    len_s = len(s)
    for i in range(1, len_s):
        sud_s_len = i + 1
        possible_opt = len_s - sud_s_len + 1
        for index in range(possible_opt):
            sub_str = s[index:index + sud_s_len]
            if sub_str == sub_str[-1::-1] and len(sub_str) > len(polind_sub_str):
                polind_sub_str = sub_str
    return polind_sub_str


cases = "xaabacxcabaaxcabaax", "babad", "cbbd", "abcdefg", 

for i in cases:
    print(longestPalindrome(i))
