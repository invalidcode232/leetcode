m = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}


def xnor(a, b) -> bool:
    return not (a ^ b)


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        a1, a2 = m[coordinate1[0]], int(coordinate1[1])

        b1, b2 = m[coordinate2[0]], int(coordinate2[1])

        return xnor(xnor(a1 % 2 == 0, a2 % 2 == 0), xnor(b1 % 2 == 0, b2 % 2 == 0))
