class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        res = []
        dp = {}

        for q in queries:
            best = 0

            if q in dp:
                res.append(dp[q])
                continue

            for item in items:
                if item[0] <= q:
                    best = max(best, item[1])

            dp[q] = best

            res.append(best)

        return res


s = Solution()
# print(s.maximumBeauty())
