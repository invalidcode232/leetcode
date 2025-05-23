class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        numbers = set()
        cur_n = n

        while True:
            s = 0
            while cur_n >= 10:
                s += (cur_n % 10) ** 2
                cur_n //= 10

            s += cur_n**2

            if s == 1:
                return True

            if s in numbers:
                return False

            numbers.add(s)
            cur_n = s

        return False


s = Solution()
print(s.isHappy(2))
