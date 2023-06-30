class Solution:
    def intToRomanD(self, num: int) -> str:
        res = ""
        d = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5:"V", 4: "IV", 1:"I"
        }
        for i in d:
            if num < i:
                continue
            c = num // i
            num = num % i
            res = res + d[i] * c
        return res
    
    def intToRomanW(self, num: int) -> str:
        res = ""
        while num:
            if num >= 1000:
                c = num // 1000
                num = num % 1000
                res = res + "M"*c
                continue
            elif num >= 900:
                c = num // 900
                num = num % 900
                res = res + "CM"
                continue
            elif num >= 500:
                c = num // 500
                num = num % 500
                res = res + "D"
                continue
            elif num >= 400:
                c = num // 400
                num = num % 400
                res = res + "CD"
                continue
            elif num >= 100:
                c = num // 100
                num = num % 100
                res = res + "C"*c
                continue
            elif num >= 90:
                c = num // 90
                num = num % 90
                res = res + "XC"
                continue
            elif num >= 50:
                c = num // 50
                num = num % 50
                res = res + "L"
                continue
            elif num >= 40:
                c = num // 40
                num = num % 40
                res = res + "XL"
                continue
            elif num >= 10:
                c = num // 10
                num = num % 10
                res = res + "X"*c
                continue
            elif num >= 9:
                c = num // 9
                num = num % 9
                res = res + "IX"
                continue
            elif num >= 5:
                c = num // 5
                num = num % 5
                res = res + "V"
                continue
            elif num >= 4:
                c = num // 4
                num = num % 4
                res = res + "IV"
                continue
            else:
                c = num // 1
                num = num % 1
                res = res + "I"*c
        return res

cases = (
    3,
    58,
    1994,
    1985,
)

results = (
    "III",
    "LVIII",
    "MCMXCIV",
    "MCMLXXXV",
)

a = Solution()
b = a.intToRomanD

for i,v in enumerate(cases):
    print(f"result: {b(v)}, expected: {results[i]}")