MIN = -1 * pow(2, 31)
MAX = pow(2, 31) - 1


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        sign = x < 0
        xs = str(x)

        if sign is True:
            xs = xs[1:]

        res = xs[::-1]

        res_f = ""
        enc_n = False
        for d in res:
            if enc_n is False and d != "0":
                enc_n = True

            if enc_n is False and d == "0":
                continue

            res_f += d

        res_f = int(res_f)

        if res_f < MIN or res_f > MAX:
            return 0

        if sign:
            return res_f * -1

        return res_f


s = Solution()
print(s.reverse(120))
