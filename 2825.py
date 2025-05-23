class Solution:
    def shift(self, c: str) -> str:
        if ord(c) == 122:
            return "a"

        return chr(ord(c) + 1)

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0

        while i <= len(str1) - 1:
            if str1[i] == str2[j] or self.shift(str1[i]) == str2[j]:
                j += 1

            if j == len(str2):
                return True

            i += 1

        return False


s = Solution()
print(s.canMakeSubsequence("ab", "d"))
