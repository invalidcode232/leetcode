class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start = 1
        end = x
        mid = -1

        while end >= start:
            # mid = int(start + (end - start) / 2)
            mid = (start + end) // 2
            # print(start, end, mid)

            cur = mid * mid

            if cur < x:
                start = mid + 1
            elif cur > x:
                end = mid - 1
            else:
                return mid

        return end


s = Solution()
print(s.mySqrt(3))
