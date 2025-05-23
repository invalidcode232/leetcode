class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maj = len(nums) // 2
        log = {}

        for n in nums:
            if n not in log:
                log[n] = 1
            else:
                log[n] += 1

                if log[n] > maj:
                    return n

        return -1


s = Solution()
print(s.majorityElement([1, 2, 1]))
