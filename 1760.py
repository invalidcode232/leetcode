import math


class Solution:
    def is_possible(self, nums: list[int], max_operations: int, ideal_num: int) -> bool:
        total_operations = 0
        for num in nums:
            total_operations += math.ceil(num / ideal_num) - 1

            if total_operations > max_operations:
                return False

        return True

    def minimumSize(self, nums: list[int], max_operations: int):
        left = 1
        right = max(nums)

        mid = 0
        while left <= right:  # get the best max_operations
            mid = (left + right) // 2

            if self.is_possible(nums, max_operations, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


s = Solution()
print(s.minimumSize([2, 4, 8, 2], 4))
