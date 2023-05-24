def convert(s: str, numRows: int) -> str:
    rows = [[] for _ in range(numRows)]
    direction = True  # True == Down; False == Up
    add_i = 0
    g_i = 0
    for i, r in enumerate(s):
        rows[g_i].append(r)
        if (i + 1 + add_i) % numRows == 0:
            direction = not direction
            add_i += 1
        if direction:
            g_i += 1
        else:
            g_i -= 1
    a = ""
    for i in rows:
        a = a + "".join(i)
    return a

cases = ("PAYPALISHIRING", 3), ("PAYPALISHIRING", 4), ("A", 1),
cdddd = ("PAHNAPLSIIGYIR", 3), ("PINALSIGYAHRPI", 4), ("A", 1),

for i in cases:
    print(convert(*i))