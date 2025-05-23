# pyright: strict


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        start = 0
        end = x
        mid = -1

        while start <= end:
            mid = (start + end) // 2

            res = mid**2

            if res == x:
                return mid

            if res > x:
                end = mid - 1
            else:
                start = mid + 1

        return end


s = Solution()
print(s.mySqrt(0))
