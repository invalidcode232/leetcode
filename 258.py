class Solution:
    def addDigits(self, num: int) -> int:
        n = str(num)

        sn = sum([int(d) for d in n])

        if sn >= 10:
            return self.addDigits(sn)
        else:
            return sn


s = Solution()
print(s.addDigits(38))
