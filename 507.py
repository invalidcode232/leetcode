class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 0

        for i in range(1, num // 2 + 1):
            if num % i == 0:
                s += i

        return s == num


s = Solution()
