class Solution:
    def generate(self, n: int) -> list[list[int]]:
        pascal: list[list[int]] = []

        for i in range(0, n + 1):
            pascal.append([])

            for j in range(i):
                if j == 0 or j == i - 1:
                    pascal[i].append(1)
                    continue

                pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])

        pascal.pop(0)

        return pascal


s = Solution()
print(s.generate(2))
