class Solution:
    def myAtoi(self, s: str) -> int:
        ne = 0
        res = 0
        for i in s:
            if not i.isdigit():
                if res or ne != 0:
                    break
                else:
                    if i == "+":
                        ne = 1
                    elif i == "-":
                        ne = -1
                    elif i == " ":
                        continue
                    else:
                        break
            else:
                if ne != -1:
                    ne = 1
                if res:
                    if (res > 2**31 // 10) or (res == 2**31 // 10 and int(i) > 7):
                        if ne < 0:
                            return -2**31
                        else:
                            return (2**31) - 1
                    res = (res * 10) + int(i)
                else:
                    res = int(i)
        return res * ne
