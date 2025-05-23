class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums) + 1

        return int(n * ((n / 2) - (1 / 2)) - sum(nums))


s = Solution()
print(s.missingNumber([3, 0, 1]))
