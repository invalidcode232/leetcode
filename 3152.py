class Solution:
    def checkArray(self, nums: list[int], query_min: int, query_max: int) -> bool:
        even = nums[query_min] % 2 == 0

        for i in range(query_min + 1, query_max + 1):
            if even:
                if nums[i] % 2 == 0:
                    return False
            else:
                if nums[i] % 2 != 0:
                    return False

            even = not even

        return True

    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        res: list[bool] = []

        for query in queries:
            res.append(self.checkArray(nums, query[0], query[1]))

        return res


s = Solution()
print(s.isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]))
print(s.isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]))
