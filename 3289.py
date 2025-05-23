from collections import Counter


class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        c = Counter(nums).items()
        return [k[0] for k in c if k[1] == 2]


s = Solution()
print(s.getSneakyNumbers([0, 1, 0]))
