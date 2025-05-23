class Solution:
    def convert(self, s: str, r: int) -> str:
        log = ["" for _ in range(r)]

        if r == 1:
            return s

        row = 0
        count = 0
        decrease = False
        while count < len(s):
            log[row] += s[count]

            count += 1

            if decrease:
                row -= 1
            else:
                row += 1

            if row == (r - 1):
                decrease = True
            elif row == 0:
                decrease = False

        res = "".join(s for s in log)

        return res


s = Solution()
print(s.convert("ab", 1))
