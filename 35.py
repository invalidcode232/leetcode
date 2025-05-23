# pyright: strict


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.append(target)

        r = sorted(nums)

        return r.index(target)
