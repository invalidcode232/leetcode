class Solution:
    def binary_search(self, start: int, end: int, indexes: list[int]) -> bool:
        left = 0
        right = len(indexes)

        while left < right:
            check = left + (left + right) // 2

            if indexes[check] < start:
                left = check + 1
            elif indexes[check] > end:
                right = check - 1
            else:
                return True

        return False

    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        res: list[bool] = []
        bads: list[int] = []

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                bads.append(i)

        for query in queries:
            search = self.binary_search(query[0] + 1, query[1], bads)

            if search:
                res.append(False)
            else:
                res.append(True)

        return res


s = Solution()
print(s.isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]))
print(s.isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]))
