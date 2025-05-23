import math

MIN = -1 * pow(2, 31)
MAX = pow(2, 31) - 1


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        res = 0
        enc_d = False
        sign = x < 0

        if sign is True:
            x *= -1

        count = int(math.log10(x))

        while x >= 10:
            d = x % 10
            x = x // 10

            if enc_d is False and x != 0:
                enc_d = True

            if enc_d is False and x == 0:
                continue

            res += d * pow(10, count)
            count -= 1

        res += x * pow(10, count)

        if sign is True:
            res *= -1

        if res > MAX or res < MIN:
            return 0

        return int(res)


s = Solution()
print(s.reverse(10))
