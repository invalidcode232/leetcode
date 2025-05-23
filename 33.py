class solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        i, j = 0, len(nums) - 1

        if nums[i] < nums[j]:  # is sorted
            while i < j:
                if nums[i] == target:
                    return i
                elif nums[j] == target:
                    return j

                if nums[i] < target:
                    i += 1
                elif nums[j] > target:
                    j -= 1
                else:
                    return -1

        while nums[i] > nums[j]:
            if nums[i] == target:
                return i
            elif nums[j] == target:
                return j

            if target < nums[i] and target > nums[j]:
                return -1

            if target > nums[i]:
                i += 1
            elif target < nums[j]:
                j -= 1

        return -1


s = solution()
print(s.search([1, 3], 3))
