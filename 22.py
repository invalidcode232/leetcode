class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res: list[str] = []

        def dfs(l: int, r: int, s: str):
            if l >= n:
                s += ")" * (n - r)
                return res.append(s)

            if l < n:
                dfs(l + 1, r, s + "(")

            if r < l:
                dfs(l, r + 1, s + ")")

        dfs(0, 0, "")

        return res


s = Solution()
print(s.generateParenthesis(3))
