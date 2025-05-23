# pyright: strict


class Solution:
    def is_same(self, s: str) -> bool:
        return s == len(s) * s[0]

    def longestPalindrome(self, s: str) -> str:
        ls = len(s)

        if len(s) == 1:
            return s

        if self.is_same(s):
            return s

        longest, longest_len = "", 0

        for i in range(ls):
            for j in range(i + 1, ls + 1):
                substring = s[i:j]

                if self.is_same(substring) or substring == substring[::-1]:
                    sub_len = len(substring)
                    if sub_len > longest_len:
                        longest_len = sub_len
                        longest = substring

        return longest


print(len(set("AAAAAAAA")))
