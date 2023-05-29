def reverse(x: int) -> int:
    sing = -1 if x < 0 else 1
    str_int = str(abs(x))
    rev_int = int(str_int[-1::-1])
    if rev_int > 2**31 - 1:
        return 0
    return rev_int * sing


cases = [123, -123, 120, 1534236469, 1563847412]

for i in cases:
    print(reverse(i))