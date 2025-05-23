class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def traverse_iter(cur_y, cur_x):
            if cur_y >= m or cur_x >= n:
                return 0

            if cur_y == (m - 1) and cur_x == (n - 1):
                return 1

            return traverse_iter(cur_y + 1, cur_x) + traverse_iter(cur_y, cur_x + 1)

        return traverse_iter(0, 0)


s = Solution()
print(s.uniquePaths(20, 10))
