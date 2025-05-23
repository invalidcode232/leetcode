class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []

        res = []

        min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                if min == nums[i - 1]:
                    res.append(f"{min}")
                else:
                    res.append(f"{min}->{nums[i - 1]}")

                min = nums[i]

        if min == nums[len(nums) - 1]:
            res.append(f"{nums[len(nums) - 1]}")
        else:
            res.append(f"{min}->{nums[len(nums) - 1]}")

        return res


i = [0, 1, 2, 4, 5, 7]
i = [0, 2, 3, 4, 6, 8, 9]
s = Solution()
print(s.summaryRanges(i))
