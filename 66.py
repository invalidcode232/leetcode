class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = 0
        ld = len(digits) - 1

        for i, val in enumerate(digits):
            n += val * pow(10, ld - i)

        n += 1

        n = str(n)
        r = [int(d) for d in n]

        return r


s = Solution()
s.plusOne([999])
