import math

ROMAN_NUMERALS = {
    0: "",
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}


class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""

        while num > 0:
            exp = int(math.log10(num))

            cur_exp = int(math.pow(10, exp))
            digit = int(num // math.pow(10, exp))

            if digit == 4:
                res += ROMAN_NUMERALS[cur_exp] + ROMAN_NUMERALS[5 * cur_exp]
            elif digit == 9:
                res += (
                    ROMAN_NUMERALS[cur_exp] + ROMAN_NUMERALS[int(math.pow(10, exp + 1))]
                )
            elif digit >= 5:
                res += ROMAN_NUMERALS[5 * cur_exp] + (
                    (digit - 5) * ROMAN_NUMERALS[cur_exp]
                )
            else:
                res += digit * ROMAN_NUMERALS[cur_exp]

            num -= digit * cur_exp

        return res


s = Solution()
print(s.intToRoman(49))
