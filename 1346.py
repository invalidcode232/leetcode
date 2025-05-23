from typing import Counter


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        c = Counter(arr)

        if c[0] > 1:
            print("hi")
            return True

        for i in arr:
            if i == 0:
                continue

            if i * 2 in c:
                return True

        return False


s = Solution()
print(s.checkIfExist([-2, 0, 10, -19, 4, 6, -8]))
