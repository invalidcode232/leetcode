class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()

        return nums[len(nums) // 2]


s = Solution()
print(s.majorityElement([1]))
