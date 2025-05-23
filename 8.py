import re

MIN = -1 * pow(2, 31)
MAX = pow(2, 31) - 1

d_r = r"\d+|$"


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if s == "":
            return 0

        n = re.findall(d_r, s)[0]

        if n == "":
            return 0

        n_i = s.find(n[0])
        f_c = s[0]

        if not (n_i == 0 or ((f_c == "-" or f_c == "+") and n_i == 1)):
            return 0

        sign = False
        if f_c == "-":
            sign = True

        res = int(n)
        if sign is True:
            res = -res

        res = min(res, MAX)
        res = max(res, MIN)

        return res


s = Solution()
print(s.myAtoi("words and 987"))
