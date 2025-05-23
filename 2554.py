class Solution:
    def maxCount(self, banned, n: int, maxSum: int) -> int:
        banned = set(banned)

        count = 0
        sum = 0
        i = 1

        while i <= n and sum + i <= maxSum:
            if i not in banned:
                sum += i
                # print(i, sum)
                count += 1

            i += 1

        return count


s = Solution()
print(s.maxCount([1, 6, 5], 5, 6))
