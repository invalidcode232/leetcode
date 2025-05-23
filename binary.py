def genBinary(n: int):
    if n == 0:
        return "0"

    b = [0]
    s = 1
    c = 0

    for _ in range(0, n):
        b[c] = s

        s += 1

        if s > 1:
            b.append(0)
            s = 0
            c += 1
