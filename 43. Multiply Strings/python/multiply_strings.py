class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        z = 48
        n1 = ord(num1[0]) - z
        n2 = ord(num2[0]) - z
        m = 10
        for i in num1[1:]:
            n1 = (n1 * m) + (ord(i) - z)
        for i in num2[1:]:
            n2 = (n2 * m) + (ord(i) - z)
        a = n1*n2
        if a == 0:
            return "0"
        sa = ""
        while a:
            c = a%m
            a = a//m
            sa = f"{c}" + sa
        return sa
