from typing import List


class Solution:
    def evalRPNC(self, tokens: List[str]) -> int:
        n = []
        for i in tokens:
            match i:
                case "+" | "-" | "*" | "/":
                    a = n.pop()
                    b = n.pop()
                    match i:
                        case "+":
                            n.append(b+a)
                        case "-":
                            n.append(b-a)
                        case "*":
                            n.append(b*a)
                        case "/":
                            n.append(int(b/a))
                case _:
                    n.append(int(i))
        return n.pop()
    
    def evalRPNI(self, tokens: List[str]) -> int:
        n = []
        for i in tokens:
            if i == "+":
                n.append(n.pop() + n.pop())
            elif i == "-":
                a = n.pop()
                b = n.pop()
                n.append(b - a)
            elif i == "*":
                n.append(n.pop() * n.pop())
            elif i == "/":
                a = n.pop()
                b = n.pop()
                n.append(int(b / a))
            else:
                n.append(int(i))
        return n.pop()

    def evalRPND(self, tokens: List[str]) -> int:
        n = []
        d = {
            "*": lambda a,b: a*b,
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "/": lambda a,b: int(a/b)
        }
        for i in tokens:
            if not i in d:
                n.append(int(i))
            else:
                x = n.pop()
                y = n.pop()
                n.append(d[i](y, x))
        return n.pop()