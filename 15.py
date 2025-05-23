# pyright: strict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res: set[tuple[int, int, int]] = set()

        for i in range(len(nums)):
            first = nums[i]
            second_i = i + 1  # Next bigger than first (but smaller than the rest)
            third_i = len(nums) - 1  # The biggest index number

            while second_i < third_i:  # first_i < second_i < third_i
                second = nums[second_i]
                third = nums[third_i]

                s = first + second + third

                if s > 0:  # third is too big
                    third_i -= 1
                elif s < 0:  # second is too small
                    second_i += 1
                else:  # we got a hit!
                    res.add((first, second, third))
                    third_i -= 1
                    second_i += 1

        return list(list(l) for l in res)


s = Solution()
inp = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(inp))
