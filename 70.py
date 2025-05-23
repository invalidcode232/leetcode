class Solution:
    def climbStairs(self, n: int):
        if n == 0 or n == 1:
            return 1

        ways = tuple([1, 1])

        for i in range(2, n + 1):
            ways = ways + (ways[i - 1] + ways[i - 2],)

        return ways[n]


s = Solution()
print(s.climbStairs(1))
# ways: tuple[int, ...] = tuple([1, 2])
# ways = ways + (3,)
# print(ways[2])
