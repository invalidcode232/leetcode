# pyright: strict


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while end >= start:
            mid = (start + end) // 2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid

        return -1


s = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(s.search(nums, target))
